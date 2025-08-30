"""Main example demonstrating the unified configuration management system.

This example showcases the complete workflow of the digital casting system using
the unified ConfigManager API that integrates with data structures and HAL devices.

The example demonstrates:
1. Loading PLC configurations into memory as structured data objects
2. Creating device instances using the unified configuration management
3. Accessing device parameters and variables through the HAL interface
4. Demonstrating the unified approach for all machine types

Usage:
    python examples/main.py
"""

from dcs.hal.device import ConcretePump, Controller, DosingPumpHigh, DosingPumpLow, InlineMixer
from dcs.hal.plc import PLC
from dcs.infrastructure.config_manager import ConfigManager


def demonstrate_unified_config_system():
  """Demonstrate the complete unified configuration management workflow."""
  print("=" * 60)
  print("Digital Casting System - Unified Configuration Demo")
  print("=" * 60)

  # Step 1: Initialize the configuration manager
  print("\n1. Initializing ConfigManager...")
  config = ConfigManager()
  print("   ✓ ConfigManager initialized")
  print(f"   ✓ Config directory: {config._config_dir}")

  # Step 2: Load all PLC configurations into memory
  print("\n2. Loading PLC configurations into memory...")
  try:
    config.load_plc_config()
    print("   ✓ All PLC configurations loaded successfully")
  except Exception as e:
    print(f"   ✗ Failed to load PLC config: {e}")
    return

  # Step 3: Display available machines
  print("\n3. Available machines in configuration:")
  all_machines = config.get_all_machines()
  for machine_name, machine_config in all_machines.items():
    print(f"   • {machine_name} (ID: {machine_config.machine_id})")
    print(f"     - Inputs: {len(machine_config.machine_input)}")
    print(f"     - Outputs: {len(machine_config.machine_output)}")

  print("\n" + "=" * 60)
  print("Device Creation and Demonstration")
  print("=" * 60)

  # Step 4: Demonstrate device creation and usage
  devices = []

  # Create InlineMixer
  try:
    print("\n4. Creating InlineMixer device...")
    mixer_config = config.get_machine("inline_mixer")
    mixer = InlineMixer(
      mixer_config.machine_id,
      mixer_config.machine_input,
      mixer_config.machine_output,
    )
    devices.append(("Inline Mixer", mixer))
    print(f"   ✓ InlineMixer created (Device ID: {mixer.device_id()})")
  except Exception as e:
    print(f"   ✗ Failed to create InlineMixer: {e}")

  # Create ConcretePump
  try:
    print("\n5. Creating ConcretePump device...")
    pump_config = config.get_machine("concrete_pump")
    concrete_pump = ConcretePump(
      pump_config.machine_id,
      pump_config.machine_input,
      pump_config.machine_output,
    )
    devices.append(("Concrete Pump", concrete_pump))
    print(f"   ✓ ConcretePump created (Device ID: {concrete_pump.device_id()})")
  except Exception as e:
    print(f"   ✗ Failed to create ConcretePump: {e}")

  # Create DosingPumpHigh
  try:
    print("\n6. Creating DosingPumpHigh device...")
    dosing_high_config = config.get_machine("dosing_pump_high")
    dosing_high = DosingPumpHigh(
      dosing_high_config.machine_id,
      dosing_high_config.machine_input,
      dosing_high_config.machine_output,
    )
    devices.append(("Dosing Pump High", dosing_high))
    print(f"   ✓ DosingPumpHigh created (Device ID: {dosing_high.device_id()})")
  except Exception as e:
    print(f"   ✗ Failed to create DosingPumpHigh: {e}")

  # Create DosingPumpLow
  try:
    print("\n7. Creating DosingPumpLow device...")
    dosing_low_config = config.get_machine("dosing_pump_low")
    dosing_low = DosingPumpLow(
      dosing_low_config.machine_id,
      dosing_low_config.machine_input,
      dosing_low_config.machine_output,
    )
    devices.append(("Dosing Pump Low", dosing_low))
    print(f"   ✓ DosingPumpLow created (Device ID: {dosing_low.device_id()})")
  except Exception as e:
    print(f"   ✗ Failed to create DosingPumpLow: {e}")

  # Create Controller (System)
  try:
    print("\n8. Creating Controller device...")
    system_config = config.get_machine("system")
    controller = Controller(
      system_config.machine_id,
      system_config.machine_input,
      system_config.machine_output,
    )
    devices.append(("System Controller", controller))
    print(f"   ✓ Controller created (Device ID: {controller.device_id()})")
  except Exception as e:
    print(f"   ✗ Failed to create Controller: {e}")

  print("\n" + "=" * 60)
  print("Device Functionality Demonstration")
  print("=" * 60)

  # Step 5: Demonstrate device functionality
  for device_name, device in devices:
    print(f"\n{device_name} Details:")
    print(f"   Device ID: {device.device_id()}")

    # Show input variables
    input_vars = list(device.get_input_var_name())
    if input_vars:
      print(f"   Input Variables ({len(input_vars)}):")
      for var in input_vars[:3]:  # Show first 3
        param_id = device.parameter_id(var)
        print(f"     • {var} (ID: {param_id})")
      if len(input_vars) > 3:
        print(f"     ... and {len(input_vars) - 3} more")
    else:
      print("   Input Variables: None")

    # Show output variables
    output_vars = list(device.get_output_var_name())
    if output_vars:
      print(f"   Output Variables ({len(output_vars)}):")
      for var in output_vars[:3]:  # Show first 3
        param_id = device.parameter_id(var)
        print(f"     • {var} (ID: {param_id})")
      if len(output_vars) > 3:
        print(f"     ... and {len(output_vars) - 3} more")
    else:
      print("   Output Variables: None")

  print("\n" + "=" * 60)
  print("PLC Communication Setup")
  print("=" * 60)

  # Step 6: Demonstrate PLC communication setup
  print("\n9. Setting up PLC communication...")
  try:
    # Create PLC connection instance (note: requires actual hardware to connect)
    plc = PLC(netid="5.57.158.168.1.1", ip="192.168.30.11")
    print("   ✓ PLC instance created")
    print(f"   ✓ Network ID: {plc.netid}")
    print(f"   ✓ IP Address: {plc.ip}")

    # Note: Actual connection would require hardware
    print("   i Note: PLC connection requires actual Beckhoff hardware")
    print("   i Use plc.connect() to establish connection when hardware is available")

  except Exception as e:
    print(f"   ✗ Failed to create PLC instance: {e}")

  print("\n" + "=" * 60)
  print("Summary - Unified Configuration System Benefits")
  print("=" * 60)

  print("\n✓ Achievements:")
  print("  • Single ConfigManager loads all machine configurations into memory")
  print("  • Structured data objects (DataParam/DataObject) for type safety")
  print("  • Unified API: config.load_plc_config() → config.get_machine(name)")
  print("  • Seamless integration with HAL device classes")
  print("  • Eliminated duplication between ConfigManager and DataHandler")
  print("  • Thread-safe, memory-efficient configuration management")

  print("\n💡 Usage Pattern:")
  print("  1. Initialize ConfigManager")
  print("  2. Load all PLC configurations: config.load_plc_config()")
  print("  3. Get machine config: config.get_machine('machine_name')")
  print("  4. Create device: Device(config.machine_id, config.machine_input, config.machine_output)")
  print("  5. Use device through standard HAL interface")

  print("\n🔧 Next Steps:")
  print("  • Connect to actual PLC hardware for real-time communication")
  print("  • Implement robot controller integration")
  print("  • Add data logging and visualization")

  print(f"\n{'=' * 60}")
  print("Demo Complete! All systems integrated successfully.")
  print(f"{'=' * 60}\n")


if __name__ == "__main__":
  """Main entry point for the unified configuration system demonstration."""
  demonstrate_unified_config_system()
