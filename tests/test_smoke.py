from pathlib import Path
import subprocess, sys
def test_generator_and_pipeline_smoke():
    subprocess.run([sys.executable,"-m","src.generate_data","--rows","300","--output","data/raw/test.csv"],check=True)
    if Path("src/pipeline.py").exists():
        subprocess.run([sys.executable,"-m","src.pipeline"],check=True)
