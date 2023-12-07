from pathlib import Path
from typing import Union
import yaml

class MyDumper(yaml.Dumper):
    def choose_scalar_style(self) -> str:
        if self.analysis is None:
            self.analysis = self.analyze_scalar(self.event.value)

        if self.analysis.multiline or len(self.event.value) > self.best_width:
            return '>'
        
        return super().choose_scalar_style()

class YmlWriter:
    @staticmethod
    def writeYmlFile(file_path: Union[str, Path], obj: dict) -> None:
        with open(file_path, "w", encoding='utf-8') as outfile:
            yaml.dump(obj, outfile, default_flow_style=False, sort_keys=False, Dumper=MyDumper, width=80)
