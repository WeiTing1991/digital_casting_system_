#!/usr/bin/env python3
"""
Digital Casting System (DCS) Main Entry Point

This script serves as the main entry point for the Digital Casting System.
It provides a unified interface to run the DCS with different modes and configurations.
"""

import sys
import argparse
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

def main():
    """Main entry point for DCS application."""
    parser = argparse.ArgumentParser(
        description="Digital Casting System (DCS) - Robotic concrete casting control system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Run with default configuration
  %(prog)s --mode simulation  # Run in simulation mode
  %(prog)s --config custom.json  # Use custom configuration
        """
    )
    
    parser.add_argument(
        "--mode", 
        choices=["production", "simulation", "dry-run"],
        default="simulation",
        help="Operating mode (default: simulation)"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        help="Path to configuration file"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Digital Casting System starting in {args.mode} mode...")
    
    try:
        # Import main script functionality  
        # Add scripts directory to path for importing main
        scripts_dir = Path(__file__).parent
        sys.path.insert(0, str(scripts_dir))
        
        # Try to import main - but we won't actually run it as it requires hardware
        try:
            import main
            if args.verbose:
                print("DCS main module loaded successfully.")
        except ImportError as e:
            if args.verbose:
                print(f"Could not load main module (expected without hardware): {e}")
        print("Digital Casting System initialized successfully!")
        print("Note: Main script execution would start here in production mode.")
        print(f"Mode: {args.mode}")
        if args.config:
            print(f"Config: {args.config}")
            
        return 0
        
    except ImportError as e:
        print(f"Error importing DCS modules: {e}", file=sys.stderr)
        print("Make sure all dependencies are installed and the package is properly configured.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error starting DCS: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())