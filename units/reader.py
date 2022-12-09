import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy
from pathlib import Path


class ReadCsv:
    """Класс для чтения CSV файла для построения графика"""
    df: pd.DataFrame = None
    filename: str = ''
    sep: str = ';'

    def __init__(
            self,
            filename: str,
            sep: str = ';') -> None:
        self.sep = sep
        self.filename = filename
        self._load()

    def _load(self) -> None:
        if not Path(self.filename).is_file():
            raise FileNotFoundError(f'Файл {self.filename} не найден')
        self.df = pd.read_csv(self.filename, sep=self.sep)

    def update(self) -> None:
        self._load()

    def read(self) -> pd.DataFrame:
        return self.df

    def read_group(self, group_id: int) -> pd.DataFrame:
        return self._get_grouped().get_group(group_id)

    def get_groups(self) -> list[int]:
        # print(self._get_grouped().keys())
        return [key for key, item in self._get_grouped()]

    def _get_grouped(self) -> DataFrameGroupBy:
        return self.df.groupby(by=['group_id'])
