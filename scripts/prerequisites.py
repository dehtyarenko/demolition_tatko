import nande

# constants
PROPERTIES_FILE_NAME = "resources//google_drive.properties"
LOCAL_PROPS_FILE_NAME = "resources//local.properties"
FILE_ID_KEY = "file_id"
CN_API_KEY_KEY = "encripted_api_key"
SEED = "seed"

# property data collection
properties_map = nande.load_properties_files(PROPERTIES_FILE_NAME, LOCAL_PROPS_FILE_NAME)
file_id = properties_map.get(FILE_ID_KEY)
en_api_key = properties_map.get(CN_API_KEY_KEY)
seed = properties_map.get(SEED)

# data retrieval and storage
api_key = nande.decrypt(en_api_key, seed)
print("I wont share the api_key with you as you will use it download forbidden japan pron with it")
nande.read_large_file(file_id, api_key)

