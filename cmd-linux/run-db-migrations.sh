# For more information:
# https://docs.djangoproject.com/en/4.1/topics/migrations/

len=0
while ((len<=0))
do
    read -p "Migration's name: " name
    len=`expr length "$name"`
done

python src/manage.py makemigrations --name $name default_app
