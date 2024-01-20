
def recomend_location(loaction):
    province= ['Koshi','Madhesh','Bagmati','Gandaki','Lumbini','Karnali','Sudurpashchim']

def soil_infO(soil):
    allsoil={
    'Kalo': 'High fertility, excellent for various crops. Well-draining soil suitable for a wide range of crops.',
    'Rato': 'Variable fertility, moderate to high suitability. Suitable for crops with proper management practices; may require soil amendments.',
    'Haluka': 'Moderate fertility, good for cultivation. Light and suitable for crops like millets, lentils, and vegetables.',
    'Khairo': 'High fertility, excellent for various crops. Rich in nutrients, suitable for rice, wheat, and other staple crops.',
    'Phusro': 'Variable fertility, may have drainage issues. May require soil amendments; suitable for cotton, chickpeas, and cabbage.',
    'Kharani': 'Moderate fertility, good for cultivation. Suitable for a variety of crops, including wheat, rice, and potatoes.',
    'Jogi': 'Variable fertility, may be nutrient-poor. May require nutrient management; suitable for turmeric, ginger, and groundnuts.',
    }
    first_soil_only = soil.split(' ')[0]
    print(first_soil_only)
    selected_soil_crop_list =allsoil[first_soil_only]
    return(selected_soil_crop_list)

def recommend_crops(soil_type):
    soil_crops = {
    'Kalo': ['Cotton', 'Soybeans', 'Wheat', 'Sugarcane', 'Mustard', ],

    'Rato': ['Tomatoes', 'Chilies', 'Potatoes', 'Maize', 'Groundnuts'],

    'Haluka': ['Wheat', 'Millets', 'Chickpeas', 'Lentils', 'Barley'],

    'Khairo': ['Rice', 'Wheat', 'Sugarcane', 'Peanuts', 'Sesame', ],

    'Phusro': ['Cotton', 'Sunflower', 'Chickpeas', 'Millets', 'Mustard'],

    'Kharani': ['Wheat', 'Rice', 'Barley', 'Chickpeas', 'Lentils'],

    'Jogi': ['Turmeric', 'Ginger', 'Maize', 'Groundnuts', 'Millets']}

    first_soil_only = soil_type.split(' ')[0]
    selected_soil_crop_list =soil_crops[first_soil_only]
    return(selected_soil_crop_list)

def productive_quality(soil_type):
    spercentage_list = {
    'Kalo': [80, 90],
    'Rato': [65, 80],
    'Haluka': [55, 70],
    'Khairo': [80, 90],
    'Phusro': [45, 60],
    'Kharani': [55, 70],
    'Jogi': [45, 60],
}

    first_soil_only = soil_type.split(' ')[0]
    
    selected_soil_crop_productive_percentage =spercentage_list[first_soil_only]
    return(selected_soil_crop_productive_percentage)

def recomend_medicine(crop):
    crop_medicines = {
    'Cotton': ['Fertilizer A', 'Pesticide X'],
    'Soybeans': ['Fertilizer B', 'Pesticide Y'],
    'Wheat': ['Fertilizer C', 'Pesticide Z'],
    'Sugarcane': ['Fertilizer D', 'Pesticide A'],
    'Mustard': ['Fertilizer E', 'Pesticide B'],
    'Chickpeas': ['Fertilizer F', 'Pesticide C'],
    'Lentils': ['Fertilizer G', 'Pesticide D'],
    'Barley': ['Fertilizer H', 'Pesticide E'],
    'Sunflower': ['Fertilizer I', 'Pesticide F'],
    'Sesame': ['Fertilizer J', 'Pesticide G'],
    'Tomatoes': ['Fertilizer A', 'Pesticide X'],
    'Chilies': ['Fertilizer B', 'Pesticide Y'],
    'Potatoes': ['Fertilizer C', 'Pesticide Z'],
    'Maize': ['Fertilizer D', 'Pesticide A'],
    'Groundnuts': ['Fertilizer E', 'Pesticide B'],
    'Sweet Potatoes': ['Fertilizer F', 'Pesticide C'],
    'Millets': ['Fertilizer B', 'Pesticide Y'],  
    'Rice': ['Fertilizer B', 'Pesticide Y'],  
    'Linseed': ['Fertilizer I', 'Pesticide F'], 
    'Peas': ['Fertilizer D', 'Pesticide A'], 
    'Spinach': ['Fertilizer E', 'Pesticide B'], 
    'Tobacco': ['Fertilizer A', 'Pesticide X'],
    'Sorghum': ['Fertilizer E', 'Pesticide B'],
    'Cabbage': ['Fertilizer C', 'Pesticide Z'],
    'Radishes': ['Fertilizer E', 'Pesticide B'],
    'Peanuts': ['Fertilizer H', 'Pesticide E'],
    'Cumin': ['Fertilizer E', 'Pesticide B'],
    'Carrots': ['Fertilizer J', 'Pesticide G'],
    'Turmeric': ['Fertilizer A', 'Pesticide X'],
    'Ginger': ['Fertilizer B', 'Pesticide Y'],
    'Cauliflower': ['Fertilizer D', 'Pesticide A'],
    'Linseed': ['Fertilizer I', 'Pesticide F'],
}
    return (crop_medicines[crop])

def recomend_tools(crop):
    tools_for_crops = {
    'Cotton': ['Sowel', 'Chisel Plow', 'Seed Drill'],
    'Soybeans': ['Gadyanchi', 'Harro', 'Seed Drill'],
    'Wheat': ['Harro', 'Seed Drill', 'Bael'],
    'Sugarcane': ['Kudal', 'Bael', 'Crop Ferry'],
    'Mustard': ['Harro', 'Seed Drill', 'Kudal'],
    'Chickpeas': ['Kudal', 'Seed Drill', 'Gadyanchi'],
    'Lentils': ['Seed Drill', 'Kudal', 'Gadyanchi'],
    'Barley': ['Harro', 'Seed Drill', 'Kudal'],
    'Sunflower': ['Gadyanchi', 'Harro', 'Seed Drill'],
    'Sesame': ['Kudal', 'Gadyanchi', 'Seed Drill'],
    'Tomatoes': ['Bael', 'Seed Drill', 'Harro'],
    'Chilies': ['Kudal', 'Gadyanchi', 'Harro'],
    'Potatoes': ['Kudal', 'Bael', 'Seed Drill'],
    'Maize': ['Harro', 'Seed Drill', 'Kudal'],
    'Groundnuts': ['Seed Drill', 'Kudal', 'Gadyanchi'],
    'Sweet Potatoes': ['Kudal', 'Gadyanchi', 'Harro'],
    'Millets': ['Harro', 'Seed Drill', 'Kudal'],  
    'Rice': ['Seed Drill', 'Kudal', 'Gadyanchi'],  
    'Linseed': ['Harro', 'Seed Drill', 'Bael'], 
    'Peas': ['Seed Drill', 'Kudal', 'Gadyanchi'], 
    'Spinach': ['Kudal', 'Seed Drill', 'Gadyanchi'], 
    'Tobacco': ['Kudal', 'Seed Drill', 'Bael'],
    'Sorghum': ['Harro', 'Seed Drill', 'Kudal'],
    'Cabbage': ['Kudal', 'Gadyanchi', 'Harro'],
    'Radishes': ['Kudal', 'Gadyanchi', 'Harro'],
    'Peanuts': ['Kudal', 'Seed Drill', 'Gadyanchi'],
    'Cumin': ['Kudal', 'Seed Drill', 'Gadyanchi'],
    'Carrots': ['Kudal', 'Gadyanchi', 'Harro'],
    'Turmeric': ['Kudal', 'Seed Drill', 'Bael'],
    'Ginger': ['Kudal', 'Gadyanchi', 'Seed Drill'],
    'Cauliflower': ['Kudal', 'Gadyanchi', 'Harro'],
    'Linseed': ['Harro', 'Seed Drill', 'Bael'],
}

    return tools_for_crops[crop]

def soil_safety_guidelines(crop):
    soil_safety_guidelines = {
    'Kalo': {
        'description': 'Black soil is rich in organic matter and minerals. It is suitable for various crops.',
        'things_to_do': ['Regularly monitor moisture levels.', 'Implement proper drainage systems.'],
        'things_not_to_do': ['Avoid over-watering.', 'Avoid excessive use of chemical fertilizers.']
    },

    'Rato': {
        'description': 'Red soil is well-draining but may be nutrient-poor. It is suitable for certain crops.',
        'things_to_do': ['Improve soil fertility with organic matter.', 'Practice crop rotation.'],
        'things_not_to_do': ['Avoid excessive tilling.', 'Avoid leaving soil bare during the offseason.']
    },

    'Haluka': {
        'description': 'Light red soil is suitable for a variety of crops and is moderately fertile.',
        'things_to_do': ['Implement proper irrigation practices.', 'Use cover crops to prevent erosion.'],
        'things_not_to_do': ['Avoid waterlogging.', 'Avoid continuous cultivation of the same crop.']
    },

    'Khairo': {
        'description': 'Brown soil is fertile and well-draining. It is suitable for a range of crops.',
        'things_to_do': ['Apply organic mulch to retain moisture.', 'Practice crop diversity.'],
        'things_not_to_do': ['Avoid compacting the soil.', 'Avoid relying solely on chemical inputs.']
    },

    'Phusro': {
        'description': 'Grey soil may have poor drainage and fertility. It requires proper management.',
        'things_to_do': ['Implement effective drainage systems.', 'Add organic amendments to improve fertility.'],
        'things_not_to_do': ['Avoid waterlogging.', 'Avoid excessive use of chemical fertilizers.']
    },

    'Kharani': {
        'description': 'Light grey soil is moderately fertile. It is suitable for various crops with proper care.',
        'things_to_do': ['Practice proper crop rotation.', 'Apply green manure for soil improvement.'],
        'things_not_to_do': ['Avoid soil erosion.', 'Avoid leaving the soil bare during the offseason.']
    },

    'Jogi': {
        'description': 'Yellow soil may be nutrient-poor and requires careful management.',
        'things_to_do': ['Apply organic amendments for nutrient enrichment.', 'Implement soil conservation measures.'],
        'things_not_to_do': ['Avoid over-reliance on chemical fertilizers.', 'Avoid leaving the soil bare.']
    }
}
    first_soil_only = crop.split(' ')[0]
    selected_soil_crop_list =soil_safety_guidelines[first_soil_only]
    return(selected_soil_crop_list)


    

