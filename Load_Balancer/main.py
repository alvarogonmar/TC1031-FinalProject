from circular_list import CircularLinkedList
from animation_view import animate_round_robin
from plot_view import plot_distribution

NUM_SERVERS = 5
NUM_REQUESTS = 10000

def run_simulation(num_servers, num_requests):
    clist = CircularLinkedList()
    for server_id in range(num_servers):
        clist.append(server_id)
    counts = [0] * num_servers
    logs = []
    for req_id in range(num_requests):
        server_id = clist.next()
        counts[server_id] += 1
        logs.append((req_id, server_id))
    return counts, logs

def print_stats(counts):
    print("\nDistribución de Carga:")
    total = sum(counts)
    for server_id, c in enumerate(counts):
        print(f"Servidor {server_id + 1}: {c} requests")
    print(f"Total: {total}")

def main():
    counts, logs = run_simulation(NUM_SERVERS, NUM_REQUESTS)
    animate_round_robin(logs, NUM_SERVERS, max_frames=200, interval=80)
    print_stats(counts)
    plot_distribution(counts)

if __name__ == "__main__":
    main()
