import matplotlib.pyplot as plt

def plot_distribution(counts):
    num_servers = len(counts)
    x = list(range(num_servers))
    labels = [f"S{i + 1}" for i in x]
    plt.bar(labels, counts)
    plt.title("Distribución Final de Requests (Round Robin)")
    plt.xlabel("Servidor")
    plt.ylabel("Requests atendidos")
    plt.show()
