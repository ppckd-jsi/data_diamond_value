import kaggle

kaggle.api.authenticate() ## Se autentifica gracias al archivo alojado en ./Kaggle

kaggle.api.dataset_download_files('shivam2503/diamonds', path = 'data', unzip = True)

kaggle.api.dataset_metadata('shivam2503/diamonds', path = 'data')

infodump = kaggle.api.dataset_list(search='cut')