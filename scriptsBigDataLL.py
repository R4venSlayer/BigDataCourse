#REALIZADO POR LUIS ALBERTO LÓPEZ LÓPEZ

import boto3

#Primer punto 
print("PRIMER PUNTO")
s3 = boto3.client('s3')
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

print("")

#Segundo punto

print("SEGUNDO PUNTO")
response_2 = s3.list_objects(Bucket = "khadajhin")

print("nombre del bucket: khadajhin")
if 'Contents' in response_2:
    
    for f in response_2['Contents']:
        print(f['Key'])
else:
    print("No se encuentra ningun archivo")

#Tercer punto
print("")
print("TERCER PUNTO")
response_3 = s3.upload_file("/home/ubuntu/.aws/personajesLoL.txt","yasuojonia","personajesLoL.txt")
print("Se ha subido correctamente el archivo")

response_2 = s3.list_objects(Bucket = "yasuojonia")

print("nombre del bucket: khadajhin")
if 'Contents' in response_2:
    
    for f in response_2['Contents']:
        print(f['Key'])
else:
    print("No se encuentra ningun archivo")


#Cuarto punto
print("")
print("CUARTO PUNTO")
response_4 = s3.download_file("yasuojonia", "personajesLoL.txt", "adcarrys.txt")   
print("Se ha descargado correctamente el archivo")
