# scraping from pastpapers.co
import requests
import os
import time
# url = "https://pastpapers.co/cie/IGCSE/Computer-Science-0478/2022-May-June/0478_s22_ms_12.pdf"

# subject = ["Computer-Science-0478"]
subject = ["Chemistry-0620"]

year = ["2018","2019", "2020", "2021", "2022","2023"]



session = ["May-June", "Oct-Nov","March"]


qp_or_ms = ["qp", "ms"]

# variant = ["11", "12", "13", "21", "22", "23"]
variant = ["21","22","23","41","42","43","61","62","63"]


subject_code = "0478"

for subj in subject:
    for y in year:
        for s in session:
            for v in variant:
                for q in qp_or_ms:
                    winter_or_summer = ""
                    if s == "May-June":
                        winter_or_summer = "s"
                    elif s == "Oct-Nov":
                        winter_or_summer = "w"
                    else:
                        winter_or_summer = "m"
                    winter_or_summer = winter_or_summer+y[2:]

                    time.sleep(1)
                    url = f"https://pastpapers.co/cie/IGCSE/{subj}/{y}-{s}/0620_{winter_or_summer}_{q}_{v}.pdf"
                    response = requests.get(url)
                    if response.status_code == 200:
                        # Open PDF file in wb mode
                        subfolder = f"{y}-{s}"
                        second_subfolder = "Question_Papers" if q == "qp" else "Mark_Schemes"
                        os.makedirs(os.path.join("0620_Chemistry", subfolder, second_subfolder), exist_ok=True)
                        with open(os.path.join("0620_Chemistry",subfolder, second_subfolder, f"{subject_code}_{y}_{s}_{q}_{v}.pdf"), 'wb') as f:
                            # Write the content of the response to the file
                            f.write(response.content)
                    else:
                        print(f"Error: {url}")





