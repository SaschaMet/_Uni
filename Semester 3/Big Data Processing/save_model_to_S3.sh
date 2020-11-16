# chmod u+x save_model_to_S3.sh
s3cmd put File model/best.model.hdf5 s3://ml-scaleway-example/ --acl-public