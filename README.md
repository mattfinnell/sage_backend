# Sage Backend

Backend for the Sage Application

## Redis

Make sure to run `pdm run --venv in-project python manage.py rqworker default` to spin up several queue workers.

## Todo

OCR
- Transform result to nearest nutritional terms (lexicographical clustering?)

Nutrition Ranking
- NuVal / Nutriscore? (These seem dated and weird)
- 


## Quick response in regards to scoring individual ingredients.
- Understand Nutrient Content:
  - Review the nutritional information of the ingredient, including macronutrients (carbohydrates, proteins, and fats) and micronutrients (vitamins and minerals). Pay attention to the following:
    - Fiber content: Higher fiber content is generally healthier.
    - Protein quality: Complete proteins with all essential amino acids are better.
    - Healthy fats: Ingredients with unsaturated fats are preferred over saturated and trans fats.

- Consider Calories:
  - Evaluate the calorie content per serving. Low-calorie ingredients are generally considered healthier if they are nutrient-dense.

- Check for Additives and Preservatives:
  - Examine the ingredient list for additives, preservatives, and artificial colorings. Fewer additives usually indicate a healthier choice.

- Assess Sugar Content:
  - Look at the sugar content, including added sugars. Ingredients with lower added sugar are healthier.

- Examine Sodium Levels:
  - Evaluate the sodium (salt) content. Lower sodium levels are generally better for health.

- Analyze Processing Level:
  - Ingredients that are minimally processed or in their natural state are often healthier than highly processed ones. Whole foods tend to be healthier than refined or processed counterparts.

- Consider Allergens and Sensitivities:
  - Take into account any known food allergies or sensitivities you may have or that people consuming the food may have. Ingredients that trigger allergies or sensitivities are not considered healthy for those individuals.

- Glycemic Index (if applicable):
  - For carbohydrates, consider the glycemic index (GI), which measures how quickly a food raises blood sugar levels. Lower-GI ingredients are generally better for controlling blood sugar.

- Research Health Effects:
  - Conduct research on the specific health effects of the ingredient. Some ingredients may have unique health benefits or risks. For example, some herbs and spices are known for their antioxidant properties.

- Portion Control:
  - Keep portion sizes in mind. Even healthy ingredients can be problematic if consumed in excessive quantities.

- Consult Dietary Guidelines:
  - Refer to dietary guidelines or recommendations from reputable health organizations, such as the USDA Dietary Guidelines or WHO nutrition guidelines, to determine how an ingredient fits into a balanced diet.

- Consider Personal Goals and Dietary Needs:
  - Tailor your assessment to your specific health goals and dietary requirements. What's healthy for one person may not be the same for another.

- Use a Scoring System (Optional):
  - Create a scoring system or use existing ones like the NuVal or Nutri-Score to assign a numerical value to ingredients based on their healthiness. This can help you compare and rank different ingredients.