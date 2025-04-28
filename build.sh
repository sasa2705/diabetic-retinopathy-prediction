#!/bin/sh

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create a static home page that will act as entry point
mkdir -p staticfiles
cat > staticfiles/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Diabetic Retinopathy Prediction</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <style>
        body { padding-top: 50px; }
        .jumbotron { padding: 2rem 1rem; }
        .btn-primary { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="jumbotron bg-light p-5 rounded">
            <h1 class="display-4">Diabetic Retinopathy Prediction</h1>
            <p class="lead">
                This application predicts whether a patient will develop diabetic retinopathy based on health parameters.
            </p>
            <hr class="my-4">
            <p>For a full interactive experience, please visit our fully deployed version with backend functionality.</p>
            <p>
                <a class="btn btn-primary btn-lg" href="https://github.com/YOUR_USERNAME/diabetic-retinopathy-prediction" role="button">View on GitHub</a>
            </p>
        </div>
        
        <div class="row mt-5">
            <div class="col-md-6">
                <h2>Project Features</h2>
                <ul>
                    <li>Patient data management</li>
                    <li>Health record tracking</li>
                    <li>Retinopathy risk prediction</li>
                    <li>PDF report generation</li>
                </ul>
            </div>
            <div class="col-md-6">
                <h2>Project Description</h2>
                <p>
                    This web application uses a machine learning model to predict the risk of diabetic retinopathy 
                    based on patient parameters like age, blood pressure, and cholesterol levels.
                </p>
                <p>
                    The backend is built with Django and the prediction model is trained using scikit-learn.
                </p>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
EOF

echo "Build completed!" 