import pandas as pd

# Load dataset
df = pd.read_csv("sample_reviews.csv")

def recommend_product(brand=None, min_rating=0):
    results = df[df['rating'] >= min_rating]
    if brand:
        results = results[results['brand'].str.lower() == brand.lower()]
    
    if results.empty:
        return "No products match your criteria."
    
    recommendations = []
    for _, row in results.iterrows():
        recommendations.append(f"{row['brand']} {row['product']} (Rating: {row['rating']}/5) - {row['review_text']}")
    return "\n".join(recommendations)

def chatbot():
    print("Welcome to the Product Recommendation Chatbot! 🛒")
    print("You can ask me for product suggestions based on brand and rating.")
    print("Type 'exit' to quit.\n")

    while True:
        brand = input("Enter a brand (or leave blank for any): ")
        if brand.lower() == "exit":
            break

        try:
            min_rating = input("Enter minimum rating (0-5, leave blank for any): ")
            min_rating = int(min_rating) if min_rating else 0
        except ValueError:
            print("Please enter a valid number for rating.")
            continue

        print("\nHere are your recommendations:")
        print(recommend_product(brand if brand else None, min_rating))
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    chatbot()
