from datetime import timedelta, date, datetime
import wget

#Decipher the Information in URLs (Obtained by inspecting the data source)
base_url = "https://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/"
start_song = "daily_download_"
end_of_song = "_128"
extension = ".mp3"

#Constant values
today = datetime.now()
current_year    = int(today.strftime("%Y"))
current_month   = int(today.strftime("%m"))
current_day     = int(today.strftime("%d"))

#user parameters
#TODO: Get the parameters from input
start_dt = date(current_year, current_month, 9)
end_dt = date(current_year, current_month, current_day)
output_folder = r"C:\\LocalData\\sora\\Classic\\Daily\\"

#To get the dates within a range
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

#to get the songs url by date range
def download_in_range_date(start_dt, end_dt):
    
    for dt in daterange(start_dt, end_dt):

        song_name = start_song+ dt.strftime("%Y%m%d") + end_of_song + extension
        song_url = base_url + dt.strftime("%Y/%m/%d/") + song_name
        print(song_url)

#to get a single song
def download_in_single_date(dt, output_folder):

    song_name = start_song+ dt.strftime("%Y%m%d") + end_of_song + extension
    song_url = base_url + dt.strftime("%Y/%m/%d/") + song_name
    file_details = song_url,song_name

    get_file(file_details,output_folder)

#to download the file from the website
def get_file(file_details, output_folder):

    url         = file_details[0]
    filename    = file_details[1]

    wget.download(url,output_folder + filename)

download_in_single_date(end_dt,output_folder)