conda create -n ai4security python=3.10

conda activate

pip install flask -e .

pip install -r requirements.txt

Start with PORT xxx
    flask --app app --debug run -p 5000
