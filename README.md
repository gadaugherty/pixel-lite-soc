# Pixel-Lite-SOC
(still in development)
**Pixel-Lite-SOC** is a lightweight, GUI-based security operations center designed for educational and personal use. It integrates popular open-source tools like Snort and Wireshark to provide basic threat detection, alert visualization, and packet inspection—all from a simple, user-friendly interface.

## Features

- **Live Intrusion Detection** via Snort  
- **Log Parsing and Alert Display**  
- **Wireshark Integration** for deep packet analysis  
- **Intuitive GUI** built with Python (Tkinter or PyQt)  
- **Modular Design** for easy expansion

## Use Cases

- Students and beginners learning how SOCs operate  
- Home lab enthusiasts wanting a minimal SIEM  
- Quick prototyping for alert triage and packet analysis workflows

## Tech Stack

- **Python 3.10+**  
- **Snort 2/3** (configured as the IDS engine)  
- **Wireshark/tshark** (optional for packet analysis)  
- **Tkinter or PyQt** for the GUI  
- **SQLite** (optional, for alert history)

## Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/pixel-lite-soc.git
cd pixel-lite-soc
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure `snort` and `tshark` are installed and accessible via your system path.

## Usage

```bash
python3 pixel-lite-soc.py
```

From the GUI, you can:

- Start/stop Snort  
- View triggered alerts  
- Click on alerts to view associated packet data  
- Open packets in Wireshark for further inspection

## Screenshots

*(Include screenshots of the interface, alert view, and packet details section)*

## Roadmap

- [ ] Add rule management UI  
- [ ] Integrate syslog support  
- [ ] Export alerts to CSV  
- [ ] Docker support for portable setup  

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

## License

MIT License