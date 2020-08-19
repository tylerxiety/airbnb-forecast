from src.func_data_diagnosis import *
from src.func_data_engineering import *
import glob
import os

if __name__ == "__main__":

    # read
    log_time("Read")
    path = r'data\20'
    all_files = glob.glob(os.path.join(path, "listings*.csv"))

    cols = ['id', 'last_scraped', 'host_id', 'host_since', 'host_neighbourhood',
            'host_response_time', 'host_response_rate', 'host_acceptance_rate',
            'host_is_superhost', 'calculated_host_listings_count',
            'calculated_host_listings_count_entire_homes',
            'calculated_host_listings_count_private_rooms',
            'calculated_host_listings_count_shared_rooms',
            'host_verifications',
            'host_has_profile_pic', 'host_identity_verified',
            'street',
            'neighbourhood_cleansed', 'city', 'state', 'zipcode', 'market',
            'smart_location', 'country', 'latitude', 'longitude',
            'is_location_exact', 'property_type', 'room_type', 'accommodates',
            'bathrooms', 'bedrooms', 'beds', 'bed_type', 'amenities', 'square_feet',
            'price', 'weekly_price', 'monthly_price', 'security_deposit',
            'cleaning_fee', 'guests_included', 'extra_people', 'minimum_nights',
            'maximum_nights', 'minimum_minimum_nights', 'maximum_minimum_nights',
            'minimum_maximum_nights', 'maximum_maximum_nights',
            'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 'calendar_updated',
            'has_availability', 'availability_30', 'availability_60',
            'availability_90', 'availability_365', 'calendar_last_scraped',
            'number_of_reviews', 'number_of_reviews_ltm', 'first_review',
            'last_review', 'review_scores_rating', 'review_scores_accuracy',
            'review_scores_cleanliness', 'review_scores_checkin',
            'review_scores_communication', 'review_scores_location',
            'review_scores_value', 'instant_bookable', 'is_business_travel_ready',
            'cancellation_policy', 'require_guest_profile_picture',
            'require_guest_phone_verification',
            'reviews_per_month']

    ls_file = []
    for file in all_files:
        df = pd.read_csv(file, header=0)
        df = df[cols]
        ls_file.append(df)

    df_list = pd.concat(ls_file, axis=0, ignore_index=True)

    # cleanse
#todo: wrape up the func