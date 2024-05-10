import os
import sys
import subprocess
import logging
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

class VirtualEnvironmentManager:
    def __init__(self, env_name='venv', requirements_file='requirements.txt'):
        self.env_name = env_name
        self.env_path = Path.cwd() / self.env_name
        self.requirements_file = Path.cwd() / requirements_file
        self.setup_logger()
        self.setup_environment()

    def setup_logger(self):
        """Set up the logger for the VirtualEnvironmentManager class."""
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.StreamHandler(),
                                logging.FileHandler('environment_manager.log')
                            ])
        self.logger = logging.getLogger(self.__class__.__name__)

    def setup_environment(self):
        """Setup virtual environment and install packages."""
        if not self.env_path.exists():
            self.create_virtual_environment()
            self.install_packages()
        else:
            self.logger.info(f"Virtual environment already exists at {self.env_path}")

    def create_virtual_environment(self):
        """Create a virtual environment in the specified directory."""
        try:
            subprocess.check_call([sys.executable, '-m', 'venv', str(self.env_path)])
            self.logger.info(f"Virtual environment created at {self.env_path}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to create virtual environment: {e}")
            raise

    def install_packages(self):
        """Install packages from a requirements file."""
        if self.requirements_file.exists():
            try:
                subprocess.check_call([str(self.env_path / 'bin' / 'python'), '-m', 'pip', 'install', '-r', str(self.requirements_file)])
                self.logger.info("Dependencies installed from requirements.txt")
            except subprocess.CalledProcessError as e:
                self.logger.error(f"Failed to install packages: {e}")
                raise
        else:
            self.logger.warning("No requirements.txt found.")

# Initialize virtual environment and logging upon import
env_manager = VirtualEnvironmentManager()

# Further imports
