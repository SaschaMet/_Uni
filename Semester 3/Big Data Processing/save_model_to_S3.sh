# chmod u+x save_model_to_S3.sh
s3cmd put File model/xray_class_my_model.best.hdf5 s3://e2eml/ --acl-public