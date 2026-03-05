#  Prédiction du risque de diabète avec Machine Learning

🔗 **Application Streamlit :** https://diabetes-prediction3.streamlit.app/




##  Objectif du projet

L’objectif de ce projet est de développer un modèle de Machine Learning capable de prédire le risque de diabète à partir de données médicales de patients.

La détection précoce du diabète est un enjeu important en santé publique, car elle permet d’anticiper les complications et d’améliorer la prise en charge.



##  Modèles utilisés

Plusieurs algorithmes de classification supervisée ont été entraînés et comparés :

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  

Les modèles ont été évalués à l’aide de plusieurs métriques de performance.



##  Métriques d’évaluation

Les performances des modèles ont été analysées avec :

- Accuracy  
- Recall  
- F1-score  
- Matrice de confusion  

Suite à la comparaison des résultats, **Random Forest** a été sélectionné comme modèle final.



##  Déploiement

Le modèle final a été intégré dans une application interactive développée avec **Streamlit**.

L’application permet à l’utilisateur :

- d’entrer les informations médicales d’un patient  
- de lancer une prédiction  
- d’obtenir une estimation du risque de diabète accompagnée d’une probabilité  



##  Technologies utilisées

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  
