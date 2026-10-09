import time
import random
import statistics
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==========================================
# 1. IMPLEMENTASI INTI (DARI NOL / SCRATCH)
# ==========================================

def bfs(capacity_graph, source, sink, parent):
    """Fungsi pencarian jalur terpendek menggunakan BFS untuk Edmonds-Karp"""
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        for v, cap in capacity_graph[u].items():
            # Jika belum dikunjungi dan kapasitas sisa > 0
            if v not in visited and cap > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp_manual(graph, source, sink):
    """
    Fungsi utama Edmonds-Karp.
    Format graph: adjacency dictionary -> graph[u][v] = kapasitas awal
    """
    # Buat residual graph (graf sisa)
    # Kita menggunakan dictionary of dictionary agar efisien untuk graf berukuran besar (sparse)
    capacity = {u: {} for u in graph}
    for u in graph:
        for v, cap in graph[u].items():
            capacity[u][v] = cap
            if v not in capacity:
                capacity[v] = {}
            if u not in capacity[v]:
                capacity[v][u] = 0 # Inisialisasi edge mundur dengan 0
                
    # Pastikan source dan sink ada di dictionary
    if source not in capacity: capacity[source] = {}
    if sink not in capacity: capacity[sink] = {}

    parent = {}
    max_flow = 0
    
    # Terus iterasi selama ada augmenting path
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        # 1. Cari bottleneck (kapasitas sisa terkecil)
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
            
        max_flow += path_flow
        
        # 2. Perbarui residual graph
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow # Kurangi kapasitas maju
            capacity[v][u] += path_flow # Tambah kapasitas mundur
            v = parent[v]
            
    return max_flow

# ==========================================
# 2. TIGA KASUS UJI MANUAL (Syarat Tugas)
# ==========================================
def run_manual_test_cases():
    print("--- PENGUJIAN 3 KASUS UJI MANUAL ---")
    
    # Kasus Uji 1: Jalur Pipa Sederhana Lurus
    graph1 = {'S': {'A': 10}, 'A': {'T': 5}}
    print(f"Test 1 (Sederhana): {edmonds_karp_manual(graph1, 'S', 'T')} (Harapan: 5)")
    
    # Kasus Uji 2: Graf dengan Cabang
    graph2 = {
        'S': {'A': 10, 'B': 5},
        'A': {'B': 15, 'T': 5},
        'B': {'T': 10}
    }
    print(f"Test 2 (Bercabang): {edmonds_karp_manual(graph2, 'S', 'T')} (Harapan: 15)")
    
    # Kasus Uji 3: Graf dengan Bottleneck di Tengah
    graph3 = {
        'S': {'A': 100, 'B': 100},
        'A': {'B': 1, 'T': 100},
        'B': {'T': 100}
    }
    print(f"Test 3 (Bottleneck): {edmonds_karp_manual(graph3, 'S', 'T')} (Harapan: 200)")
    print("-" * 36 + "\n")

# ==========================================
# 3. SKENARIO EKSPERIMEN (Syarat Tugas)
# ==========================================
def generate_random_flow_network(num_nodes):
    """Menghasilkan graf berarah acak menggunakan NetworkX, diubah ke dictionary format"""
    # Menggunakan Erdős-Rényi graph, probability disesuaikan agar selalu terhubung tapi tidak terlalu padat
    prob = min(1.0, 10 / num_nodes) 
    G_nx = nx.gnp_random_graph(num_nodes, prob, directed=True)
    
    graph_dict = {i: {} for i in range(num_nodes)}
    for u, v in G_nx.edges():
        if u != v: # hindari self-loop
            graph_dict[u][v] = random.randint(1, 100) # Kapasitas acak 1-100
            
    return graph_dict, G_nx

def run_experiment():
    print("--- MEMULAI EKSPERIMEN KINERJA ---")
    # 5 Variasi Ukuran Input (Nodes) - Diatur agar runtime wajar
    # Sesuai syarat >= 5 ukuran input
    node_sizes = [50, 100, 200, 400, 800] 
    repeats = 5 # Syarat pengulangan >= 5x
    
    avg_times_manual = []
    std_times_manual = []
    avg_times_nx = [] # Sebagai pembanding
    
    for size in node_sizes:
        times_manual = []
        times_nx = []
        
        print(f"Menguji Graf dengan {size} simpul...")
        for _ in range(repeats):
            # 1. Siapkan Graf Acak
            graph_dict, G_nx = generate_random_flow_network(size)
            source, sink = 0, size - 1
            
            # Pastikan source & sink ada edge-nya agar fair
            if sink not in graph_dict[source]:
                graph_dict[source][sink] = random.randint(1, 100)
                G_nx.add_edge(source, sink, capacity=graph_dict[source][sink])
            
            # Setup bobot kapasitas untuk NetworkX
            nx.set_edge_attributes(G_nx, 0, 'capacity')
            for u in graph_dict:
                for v, cap in graph_dict[u].items():
                    G_nx[u][v]['capacity'] = cap
            
            # 2. Uji Kode Manual
            start_time = time.perf_counter()
            flow_manual = edmonds_karp_manual(graph_dict, source, sink)
            times_manual.append(time.perf_counter() - start_time)
            
            # 3. Uji Kode Pembanding (NetworkX)
            start_time = time.perf_counter()
            flow_nx, _ = nx.maximum_flow(G_nx, source, sink)
            times_nx.append(time.perf_counter() - start_time)
            
            # Verifikasi Integritas
            assert flow_manual == flow_nx, "HASIL TIDAK SAMA! Ada bug di algoritma manual."

        # Kalkulasi statistik
        avg_times_manual.append(statistics.mean(times_manual))
        std_times_manual.append(statistics.stdev(times_manual))
        avg_times_nx.append(statistics.mean(times_nx))
        
        print(f" Selesai | Manual: {avg_times_manual[-1]:.5f}s | NX: {avg_times_nx[-1]:.5f}s")
        
    # Plotting Grafik
    plt.figure(figsize=(10, 6))
    
    # Plot data eksperimen
    plt.errorbar(node_sizes, avg_times_manual, yerr=std_times_manual, 
                 label='Manual Edmonds-Karp', marker='o', capsize=5)
    plt.plot(node_sizes, avg_times_nx, label='NetworkX (Pembanding)', marker='s', linestyle='--')
    
    # Plot estimasi teoretis O(V*E^2) sebagai tren referensi
    # Kita skalakan agar muat dalam plot yang sama
    theoretical = [(V * (V*2)**2) for V in node_sizes] # Asumsi E sebanding dengan V*2 pada graf sparse kita
    scale_factor = avg_times_manual[-1] / theoretical[-1]
    theoretical_scaled = [t * scale_factor for t in theoretical]
    plt.plot(node_sizes, theoretical_scaled, label='Teoretis O(V*E^2) berskala', linestyle=':', color='gray')

    plt.title('Eksperimen Waktu Eksekusi: Edmonds-Karp')
    plt.xlabel('Jumlah Simpul (V)')
    plt.ylabel('Waktu Eksekusi Rata-rata (detik)')
    plt.legend()
    plt.grid(True)
    plt.savefig('hasil_eksperimen.png') # Simpan gambar grafik
    plt.show()

if __name__ == "__main__":
    run_manual_test_cases()
    run_experiment()