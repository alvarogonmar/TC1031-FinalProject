import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_round_robin(logs, num_servers, max_frames=200, interval=100):
    if not logs:
        print("No hay logs")
        return None

    counts = [0] * num_servers
    frames = min(max_frames, len(logs))

    fig, ax = plt.subplots()
    x = list(range(num_servers))
    bars = ax.bar(x, counts)

    ax.set_ylim(0, frames)
    ax.set_xlabel("Servidor")
    ax.set_ylabel("Requests atendidos")
    ax.set_title("Animación Round Robin")
    ax.set_xticks(x)
    ax.set_xticklabels([f"S{i + 1}" for i in x])

    def update(frame):
        req_id, server_id = logs[frame]
        counts[server_id] += 1

        for i, b in enumerate(bars):
            b.set_height(counts[i])

        ax.set_title(
            f"Animación Round Robin - Request {req_id} Servidor {server_id} "
            f"({frame + 1}/{frames})"
        )
        return bars

    animation = FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=interval,
        blit=False,
        repeat=False,
    )

    plt.tight_layout()
    plt.show()

    return animation
