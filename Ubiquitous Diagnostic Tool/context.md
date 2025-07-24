What Is the Ultimate Goal of This Project?

The main goal of this project is to create a **user-friendly tool** that helps anyone—whether you’re a student, hobbyist, or professional—**understand, test, and troubleshoot the electronic systems inside modern vehicles**.
 Why Is This Tool Needed?

Modern cars are like computers on wheels. They have many small computers (called ECUs—Electronic Control Units) that control everything from the engine to the air conditioning. These ECUs talk to each other using a network called **CAN** (Controller Area Network).

When something goes wrong, the car stores special error codes (called **Diagnostic Trouble Codes**, or DTCs) inside these ECUs. Mechanics use expensive, brand-specific tools to read these codes and figure out what’s wrong. But these tools are often:
- **Very expensive**
- **Difficult to use**
- **Not customizable** (you can’t add your own features or test new ideas)
- **Locked down** (you can’t see how they work inside)

### What Does This Project Do?

This project gives you an **open, flexible, and easy-to-use tool** to:
- **Read and clear error codes** from your car’s computers
- **Send special commands** to test how your car responds (for example, resetting a computer or asking for specific information)
- **Simulate new sensors** (pretend a new part is connected, to see how the car would react)
- **Test how your car handles errors** by intentionally sending wrong or unexpected messages
- **Work with real cars or in a fully simulated mode** (so you can learn and experiment safely, even without a car)

### Who Is This For?

- **Students** who want to learn how cars’ electronics work
- **Hobbyists** who want to tinker with their own vehicles
- **Engineers and developers** who want to test new ideas or parts
- **Anyone** who wants to understand or improve vehicle diagnostics

### How Is It Different from Other Tools?

- **It’s open and customizable:** You can see how everything works, add your own features, or change how it looks and behaves.
- **It’s affordable:** You don’t need to buy expensive hardware or software.
- **It’s educational:** You can use it in a safe, simulated environment to learn and experiment without risk.

### What Can You Do With It?

- **Read error codes** to find out why a warning light is on
- **Clear error codes** after fixing a problem
- **Test how your car’s computers respond** to different commands
- **Simulate new sensors or faults** to see what would happen
- **Log and review all actions** for learning or troubleshooting

### The Big Picture

This tool is like a “Swiss Army knife” for car electronics. It helps you:
- **Understand** what’s happening inside your car
- **Experiment** with new ideas or parts
- **Learn** about automotive technology in a hands-on way
- **Troubleshoot** problems without needing expensive, locked-down tools

---

Imagine you are an automotive engineer, working late in the lab. A new vehicle prototype is on the test bench, and the team is racing to diagnose a mysterious issue: the check engine light is on, but the root cause is unclear. The OEM’s diagnostic tool is locked down, expensive, and doesn’t support your custom sensors or experimental ECUs. You need to:

- Read and clear Diagnostic Trouble Codes (DTCs)
- Simulate new sensors and see how the ECU responds
- Test UDS services like ECU Reset and ReadDataByIdentifier
- Inject errors to validate robustness
- Work with both real CAN hardware and virtual/demo setups

**This is where the UDS-over-CAN Modular Tool comes in.**

It empowers engineers, testers, and students to:
- Rapidly diagnose and debug vehicles and ECUs
- Prototype and validate new sensors and UDS services
- Train and learn UDS diagnostics in a safe, simulated environment
- Extend the tool for future protocols, sensors, and services

## How to Use This Tool

### 1. Installation
- Install Python 3.8+
- Run: `pip install -r requirements.txt`
- (Optional) For GUI: ensure PyQt5 and qdarkstyle are installed

### 2. Running the GUI
- Run: `python -m gui.main_window`
- The main window opens with four tabs:
  - **UDS Requests**: Send and receive diagnostic requests
  - **Sensors**: Add, remove, simulate, and set malfunction for sensors
  - **Logs**: View recent diagnostic and system logs
  - **Settings**: Select CAN interface, enable demo mode, inject errors

#### UDS Requests Tab
- Select a UDS service (ReadDTC, ClearDTC, etc.)
- Enter request data in hex (e.g., `01` for subfunction)
- Click "Send Request" to see the response

#### Sensors Tab
- Add a sensor by ID and name
- Remove sensors
- Simulate sensor values (for demo/testing)
- Toggle malfunction state to test DTCs

#### Logs Tab
- View recent log entries
- Click "Refresh Logs" to update

#### Settings Tab
- Choose CAN interface (SocketCAN, PCAN, VirtualCAN, DemoCAN)
- Enable demo mode for full simulation (no hardware needed)
- Inject CAN or UDS errors for robustness testing
- Click "Apply Settings" to activate changes

### 3. Running the CLI
- Run: `python -m cli.main [COMMAND] [ARGS...]`
- See `docs/USAGE.md` for all commands

### 4. Example Scenarios
- **Diagnosing a real vehicle**: Connect to CAN hardware, read/clear DTCs, and log results
- **Simulating a new sensor**: Add a sensor in the GUI, simulate values, and observe UDS responses
- **Testing error handling**: Enable error injection and verify system robustness
- **Learning UDS**: Use demo mode to explore UDS services and responses without any hardware

### 5. Extending the Tool
- Add new UDS services: create a new module in `services/` inheriting from `UDSService` and register it
- Add new sensors: subclass `Sensor` and register with the `SensorRegistry`
- Add new CAN backends: implement a new class in `transports/` inheriting from `CANInterface`

## Tips
- Use demo mode for safe experimentation
- All actions are logged for traceability
- The tool is modular: you can add, remove, or swap components as needed

---

This tool bridges the gap between proprietary, inflexible diagnostic tools and the needs of modern automotive development, education, and research. Whether you’re in the lab, the classroom, or the garage, it puts the power of UDS diagnostics in your hands. 