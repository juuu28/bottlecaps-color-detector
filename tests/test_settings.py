import yaml

def test_yaml_loads():
    with open("settings.yaml", "r") as f:
        cfg = yaml.safe_load(f)
    assert "model_type" in cfg
