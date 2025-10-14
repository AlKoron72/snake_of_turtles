import pandas as pd

PATH = "50_states.csv"

class DataHandler:
    def __init__(self, source:str) -> None:
        self.source = source
        if source:
            self.data = self.load_from_csv()
        else:
            self.data = None


    def __str__(self) -> str:
        return str(self.data)

    def put_into_dataframe(self) -> pd:
        return self.data.to_dataframe()


    def load_from_csv(self) -> list[str]:
        try:
            with pd.read_csv(self.source) as file:
                return file
        except FileNotFoundError:
            print("File not found.")
            print("Please check the file path.")
            print(f"Your provided file path: {self.source}")

if __name__ == "__main__":
    data_handler = DataHandler(PATH)
    print(f"test: {data_handler.data}")