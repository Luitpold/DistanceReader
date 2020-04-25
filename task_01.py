import pandas as pd
from typing import List


class DistanceReader:

    def __init__(self):
        print("Program successfully initatied")
        df: pd.DataFrame = self.read_file_into_pandas()
        list_of_cities: List[str] = self.get_all_possible_location(df)
        self.get_result_from_selection_and_dataframe(
            df,
            self.take_input_from_user_and_validate("start", list_of_cities),
            self.take_input_from_user_and_validate("end", list_of_cities)
        )

    @staticmethod
    def read_file_into_pandas() -> pd.DataFrame:
        return pd.read_csv('entfernungen_csv.txt', sep=',', index_col=0)

    @staticmethod
    def get_all_possible_location(df: pd.DataFrame) -> List[str]:
        print("To get all destinations see list below")
        list_of_cities: List[str] = df.index.to_list()
        for city in list_of_cities:
            print(city)
        return list_of_cities

    @staticmethod
    def take_input_from_user_and_validate(usecase: str, list_of_cities: List[str]) -> str:
        value: str = input(f"Please enter a city you want to {usecase} at:\n")
        if list_of_cities.__contains__(value):
            print(f'You entered {value}')
            return value
        else:
            raise Exception("Your selection has to be in the range of available options")

    @staticmethod
    def get_result_from_selection_and_dataframe(df: pd.DataFrame, start_loc: str, end_loc: str):
        print(f"The distance between {start_loc} and {end_loc} is {df.loc[start_loc, end_loc]}")


def main():
    DistanceReader()


if __name__ == '__main__':
    main()
