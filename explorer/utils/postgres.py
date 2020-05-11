from credentials_retriever import SecretManager

print(SecretManager("dev/guillaumelegoy").retrieve_secret())