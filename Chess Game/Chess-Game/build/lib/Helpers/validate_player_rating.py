class ValidatingPlayerRating:
    def validate_rating(rating):
        try:
            rating = int(rating)
            return 0 <= rating <= 10000
        except ValueError:
            return False