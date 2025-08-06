from typing import Any
import subprocess
from pathlib import Path
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("k6")

async def run_k6_script(script_file: str, duration: str = "30s", vus: int = 10) -> str:
    """Run a k6 load test script.

    Args:
        script_file: Path to the k6 test script (.js)
        duration: Duration of the test (e.g., "30s", "1m", "5m")
        vus: Number of virtual users to simulate

    Returns:
        str: k6 execution output
    """
    try:
        # Convert to absolute path
        script_file_path = Path(script_file).resolve()
        
        # Validate file exists and is a .js file
        if not script_file_path.exists():
            return f"Error: Script file not found: {script_file}"
        if not script_file_path.suffix == '.js':
            return f"Error: Invalid file type. Expected .js file: {script_file}"

        # Use k6 directly since it's in PATH
        k6_bin = 'k6'
        
        # Build command as a string for PowerShell execution on Windows
        cmd_str = f'& "{k6_bin}" run -d {duration} -u {vus} "{script_file_path}"'
        
        # Use PowerShell on Windows for better compatibility
        powershell_cmd = ['powershell', '-Command', cmd_str]

        # Print the full command for debugging
        print(f"Executing PowerShell command: {cmd_str}")
        
        # Run the command and capture output
        result = subprocess.run(powershell_cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode != 0:
            return f"Error executing k6 test:\n{result.stderr}"
        
        return result.stdout

    except Exception as e:
        return f"Unexpected error: {str(e)}"

async def run_k6_ramping_script(script_file: str, ramp_up_duration: str, sustain_duration: str, ramp_down_duration: str, max_vus: int) -> str:
    """Run a k6 load test script with ramping configuration.

    Args:
        script_file: Path to the k6 test script (.js)
        ramp_up_duration: Duration to ramp up to max VUs (e.g., "30s", "1m")
        sustain_duration: Duration to sustain max VUs (e.g., "30s", "1m")
        ramp_down_duration: Duration to ramp down to 0 VUs (e.g., "30s", "1m")
        max_vus: Maximum number of virtual users

    Returns:
        str: k6 execution output
    """
    try:
        # Convert to absolute path
        script_file_path = Path(script_file).resolve()
        
        # Validate file exists and is a .js file
        if not script_file_path.exists():
            return f"Error: Script file not found: {script_file}"
        if not script_file_path.suffix == '.js':
            return f"Error: Invalid file type. Expected .js file: {script_file}"

        # Use k6 directly since it's in PATH
        k6_bin = 'k6'
        
        # Create ramping stages configuration
        stages = f"--stage {ramp_up_duration}:{max_vus} --stage {sustain_duration}:{max_vus} --stage {ramp_down_duration}:0"
        
        # Build command as a string for PowerShell execution on Windows
        cmd_str = f'& "{k6_bin}" run {stages} "{script_file_path}"'
        
        # Use PowerShell on Windows for better compatibility
        powershell_cmd = ['powershell', '-Command', cmd_str]

        # Print the full command for debugging
        print(f"Executing PowerShell ramping command: {cmd_str}")
        
        # Run the command and capture output
        result = subprocess.run(powershell_cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode != 0:
            return f"Error executing k6 ramping test:\n{result.stderr}"
        
        return result.stdout

    except Exception as e:
        return f"Unexpected error: {str(e)}"

async def run_k6_shared_iterations_script(script_file: str, total_iterations: int, vus: int) -> str:
    """Run a k6 load test script with shared iterations.

    Args:
        script_file: Path to the k6 test script (.js)
        total_iterations: Total number of iterations to be shared across all VUs
        vus: Number of virtual users to share the iterations

    Returns:
        str: k6 execution output
    """
    try:
        # Convert to absolute path
        script_file_path = Path(script_file).resolve()
        
        # Validate file exists and is a .js file
        if not script_file_path.exists():
            return f"Error: Script file not found: {script_file}"
        if not script_file_path.suffix == '.js':
            return f"Error: Invalid file type. Expected .js file: {script_file}"

        # Use k6 directly since it's in PATH
        k6_bin = 'k6'
        
        # Build command with shared iterations
        cmd_str = f'& "{k6_bin}" run --iterations {total_iterations} --vus {vus} "{script_file_path}"'
        
        # Use PowerShell on Windows for better compatibility
        powershell_cmd = ['powershell', '-Command', cmd_str]

        # Print the full command for debugging
        print(f"Executing PowerShell shared iterations command: {cmd_str}")
        
        # Run the command and capture output
        result = subprocess.run(powershell_cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode != 0:
            return f"Error executing k6 shared iterations test:\n{result.stderr}"
        
        return result.stdout

    except Exception as e:
        return f"Unexpected error: {str(e)}"

@mcp.tool()
async def execute_k6_test(script_file: str, duration: str = "30s", vus: int = 10) -> str:
    """Execute a k6 load test.

    Args:
        script_file: Path to the k6 test script (.js)
        duration: Duration of the test (e.g., "30s", "1m", "5m")
        vus: Number of virtual users to simulate
    """
    return await run_k6_script(script_file, duration, vus)

@mcp.tool()
async def execute_k6_test_with_options(script_file: str, duration: str, vus: int) -> str:
    """Execute a k6 load test with custom duration and VUs.

    Args:
        script_file: Path to the k6 test script (.js)
        duration: Duration of the test (e.g., "30s", "1m", "5m")
        vus: Number of virtual users to simulate
    """
    return await run_k6_script(script_file, duration, vus)

@mcp.tool()
async def execute_k6_ramping_test(script_file: str, max_vus: int, ramp_up_duration: str = "10s", sustain_duration: str = "30s", ramp_down_duration: str = "10s") -> str:
    """Execute a k6 load test with ramping virtual users (ramp up, sustain, ramp down).

    Args:
        script_file: Path to the k6 test script (.js)
        max_vus: Maximum number of virtual users to ramp up to
        ramp_up_duration: Duration to ramp up to max VUs (e.g., "10s", "30s", "1m")
        sustain_duration: Duration to sustain max VUs (e.g., "30s", "1m", "2m")
        ramp_down_duration: Duration to ramp down to 0 VUs (e.g., "10s", "30s")
    """
    return await run_k6_ramping_script(script_file, ramp_up_duration, sustain_duration, ramp_down_duration, max_vus)

@mcp.tool()
async def execute_k6_shared_iterations_test(script_file: str, total_iterations: int, vus: int) -> str:
    """Execute a k6 load test with shared iterations across all VUs.

    Args:
        script_file: Path to the k6 test script (.js)
        total_iterations: Total number of iterations to be shared across all VUs
        vus: Number of virtual users to share the iterations
    """
    return await run_k6_shared_iterations_script(script_file, total_iterations, vus)

if __name__ == "__main__":
    mcp.run(transport='stdio') 