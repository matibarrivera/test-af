from azure.storage.blob import BlobServiceClient
import os


blob_conn_str = os.getenv('BLOBCONNSTR')
blob_container = os.getenv('BLOBCONTAINER')


def read_week_config():
    week_config = "config_semana.txt"
    blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)

    container_client = blob_service_client.get_container_client(blob_container)

    try:
        blob_client = container_client.get_blob_client(week_config)
        # Read the content of the blob
        blob_data = blob_client.download_blob().readall()
    except:
        return None

    data = blob_data.decode("utf-8")
    data = data.replace(" ", "")
    data = data.split(",")
    return data