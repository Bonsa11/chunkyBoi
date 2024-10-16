from datetime import datetime
from fit_tool.fit_file_builder import FitFileBuilder # type: ignore
from fit_tool.profile.messages.file_id_message import FileIdMessage # type: ignore
from fit_tool.profile.messages.weight_scale_message import WeightScaleMessage # type: ignore
from fit_tool.profile.profile_type import Weight, Manufacturer, FileType # type: ignore

# https://bitbucket.org/stagescycling/python_fit_tool/src/main/

data = {
  "weight": 70.5,
  "percent_fat": 20.0,
  "percent_hydration": 60.0,
  "visceral_fat_mass": 12.0,
  "bone_mass": 3.0,
  "muscle_mass": 30.0,
}

def main():
    file_id_message = FileIdMessage()
    file_id_message.type = FileType.WEIGHT
    file_id_message.manufacturer = Manufacturer.DEVELOPMENT.value
    file_id_message.product = 0
    file_id_message.time_created = round(datetime.now().timestamp() * 1000)
    file_id_message.serial_number = 0x12345678

    weight_message = WeightScaleMessage()
    weight_message.timestamp = round(datetime.now().timestamp() * 1000)
    weight_message.weight = data["weight"]
    weight_message.percent_fat = data["percent_fat"]

    builder = FitFileBuilder(auto_define=True, min_string_size=50)
    builder.add(file_id_message)
    builder.add(weight_message)

    fit_file = builder.build()

    out_path = './data/fit/weight.fit'
    fit_file.to_file(out_path)


if __name__ == "__main__":
    main()