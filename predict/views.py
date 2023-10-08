from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import result1


from joblib import load

ann = load('/home/gunes/Bitirme/django-venv/src/churn/savedModels/ann.joblib')
DTmodel = load('/home/gunes/Bitirme/django-venv/src/churn/savedModels/DT.joblib')
NBmodel = load('/home/gunes/Bitirme/django-venv/src/churn/savedModels/NB.joblib')
RFmodel = load('/home/gunes/Bitirme/django-venv/src/churn/savedModels/RF.joblib')
XGBmodel = load('/home/gunes/Bitirme/django-venv/src/churn/savedModels/xgboost.joblib')

def predict(request):
    return render(request,'/home/gunes/Bitirme/django-venv/src/churn/templates/index.html')


def result(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        days_since_last_login = request.POST.get('days_last_login')
        avg_time_spent = request.POST.get('time_spent')
        avg_transaction_value = request.POST.get('avg_transaction_value')
        avg_frequency_login_days = request.POST.get('avg_frequency_login_days')
        points_in_wallet = request.POST.get('points_in_wallet')
        Region_Category = request.POST.get('Region_Category')
        joined_through_referral = request.POST.get('joined_through_referral')
        membership_category = request.POST.get('membership_category')
        preferred_offer_types = request.POST.get('preferred_offer_types')
        medium_of_operation = request.POST.get('medium_of_operation')
        internet_option = request.POST.get('internet_option')
        Discount = request.POST.get('Discount')
        Offer_Application_Preference = request.POST.get('Offer_Application_Preference')
        Past_Complaint = request.POST.get('Past_Complaint')
        Complatint_Status = request.POST.get('Complatint_Status')
        Feedback = request.POST.get('Feedback')
        prediction_method = request.POST.get('Prediction')

        
        age = float(age)
        days_since_last_login = float(days_since_last_login)
        avg_time_spent = float(avg_time_spent)
        avg_transaction_value= float(avg_transaction_value)
        avg_frequency_login_days = float(avg_frequency_login_days)
        points_in_wallet = float(points_in_wallet)
        
        def predict_result(prediction_method):
            choosen_model = load(f'/home/gunes/Bitirme/django-venv/src/churn/savedModels/{prediction_method}.joblib')
            gender_M = 0
            gender_F = 0
            region_category_City = 0
            region_category_Town = 0
            region_category_Village = 0
            joined_through_referral_No = 0
            joined_through_referral_Yes = 0
            membership_category_Basic_Membership = 0
            membership_category_Gold_Membership = 0
            membership_category_No_Membership = 0
            membership_category_Platinum_Membership = 0
            membership_category_Premium_Membership = 0
            membership_category_Silver_Membership = 0
            preferred_offer_types_Credit_Debit_Card_Offers = 0
            preferred_offer_types_Gift_Vouchers_Coupons = 0
            preferred_offer_types_Without_Offers = 0
            medium_of_operation_Both = 0
            medium_of_operation_Desktop = 0
            medium_of_operation_Smartphone = 0
            internet_option_Fiber_Optic = 0
            internet_option_Mobile_Data = 0
            internet_option_Wi_Fi = 0
            used_special_discount_No= 0
            used_special_discount_Yes = 0
            offer_application_preference_No = 0
            offer_application_preference_Yes = 0
            past_complaint_No = 0
            past_complaint_Yes= 0
            complaint_status_No_Information_Available = 0
            complaint_status_Not_Applicable = 0
            complaint_status_Solved = 0
            complaint_status_Solved_in_Follow_up = 0
            complaint_status_Unsolved = 0
            feedback_No_reason_specified = 0
            feedback_Poor_Customer_Service = 0
            feedback_Poor_Product_Quality = 0
            feedback_Poor_Website = 0
            feedback_Products_always_in_Stock = 0
            feedback_Quality_Customer_Care = 0
            feedback_Reasonable_Price = 0
            feedback_Too_many_ads = 0
            feedback_User_Friendly_Website = 0
            if gender == 'Male':
                gender_M = 1
            else:
                gender_F = 1
            if Region_Category == 'City':
                region_category_City = 1
            elif Region_Category == 'Town':
                region_category_Town = 1
            else:
                region_category_Village = 1
            if joined_through_referral == 'No':
                joined_through_referral_No = 1
            else:
                joined_through_referral_Yes = 1
            if membership_category == 'Basic Membership':
                membership_category_Basic_Membership = 1
            elif membership_category == 'Silver Membership':
                membership_category_Silver_Membership = 1
            elif membership_category == 'Gold Membership':
                membership_category_Gold_Membership = 1
            elif membership_category == 'Platinum Membership':
                membership_category_Platinum_Membership = 1
            elif membership_category == 'Premium Membership':
                membership_category_Premium_Membership = 1
            else:
                membership_category_No_Membership = 1
            if preferred_offer_types == 'Credit/Debit Card Offers':
                preferred_offer_types_Credit_Debit_Card_Offers = 1
            elif preferred_offer_types == 'Vouchers/Coupons Offers':
                preferred_offer_types_Gift_Vouchers_Coupons = 1
            else:
                preferred_offer_types_Without_Offers = 1
            if medium_of_operation == 'Desktop Operation':
                medium_of_operation_Desktop = 1
            elif medium_of_operation == 'Smartphone Operation':
                medium_of_operation_Smartphone = 1
            else:
                medium_of_operation_Both = 1
            if internet_option == 'Wi-Fi':
                internet_option_Wi_Fi = 1
            elif internet_option == 'Mobile Data':
                internet_option_Mobile_Data = 1
            else:
                internet_option_Fiber_Optic = 1
            if Discount == 'No':
                used_special_discount_No = 1
            else:
                used_special_discount_Yes = 1
            if Offer_Application_Preference == 'No':
                offer_application_preference_No = 1
            else:
                offer_application_preference_Yes = 1
            if Past_Complaint == 'No':
                past_complaint_No = 1
            else:
                past_complaint_Yes = 1
            if Complatint_Status == 'No Information Avaible':
                complaint_status_No_Information_Available = 1
            elif Complatint_Status == 'Not Applicable':
                complaint_status_Not_Applicable = 1
            elif Complatint_Status == 'In Follow-Up':
                complaint_status_Solved_in_Follow_up = 1
            elif Complatint_Status == 'Solved':
                complaint_status_Solved = 1
            else:
                complaint_status_Unsolved = 1
            if Feedback == 'No Reason Specified':
                feedback_No_reason_specified = 1
            elif Feedback == 'Poor Customer Service':
                feedback_Poor_Customer_Service = 1
            elif Feedback == 'Poor Product Quality':
                feedback_Poor_Product_Quality = 1
            elif Feedback == 'Poor Website':
                feedback_Poor_Website = 1
            elif Feedback == 'Too many ads':
                feedback_Too_many_ads = 1
            elif Feedback == 'Product always in Stock':
                feedback_Products_always_in_Stock = 1
            elif Feedback == 'Quality Customer Care':
                feedback_Quality_Customer_Care = 1
            elif Feedback == 'Reasonable Price':
                feedback_Reasonable_Price = 1
            else:
                feedback_User_Friendly_Website = 1
            prediction_result = choosen_model.predict([[age,days_since_last_login,avg_time_spent,avg_transaction_value,avg_frequency_login_days,
                                                points_in_wallet,gender_F,gender_M,region_category_City,region_category_Town,region_category_Village,joined_through_referral_No,
                                                joined_through_referral_Yes,membership_category_Basic_Membership,membership_category_Gold_Membership,membership_category_No_Membership,
                                                membership_category_Platinum_Membership,membership_category_Premium_Membership,membership_category_Silver_Membership,preferred_offer_types_Credit_Debit_Card_Offers,
                                                preferred_offer_types_Gift_Vouchers_Coupons,preferred_offer_types_Without_Offers,medium_of_operation_Both,medium_of_operation_Desktop,
                                                medium_of_operation_Smartphone,internet_option_Fiber_Optic,internet_option_Mobile_Data,internet_option_Wi_Fi,used_special_discount_No,used_special_discount_Yes,
                                                offer_application_preference_No,offer_application_preference_Yes,past_complaint_No,past_complaint_Yes,complaint_status_No_Information_Available,
                                                complaint_status_Not_Applicable,complaint_status_Solved,complaint_status_Solved_in_Follow_up,complaint_status_Unsolved,feedback_No_reason_specified,
                                                feedback_Poor_Customer_Service,feedback_Poor_Product_Quality,feedback_Poor_Website,feedback_Products_always_in_Stock,feedback_Quality_Customer_Care,
                                                feedback_Reasonable_Price,feedback_Too_many_ads,feedback_User_Friendly_Website]])
            if prediction_result[0] == 1:
                prediction_result = 'Churn'
            else:
                prediction_result = 'Not Churn'
            prediction = prediction_result
            results = result1.objects.create(_gender = gender,_age = age,_days_since_last_login=days_since_last_login,_avg_time_spent=avg_time_spent,
                                        _avg_transaction_value=avg_transaction_value,_avg_frequency_login_days=avg_frequency_login_days,_points_in_wallet=points_in_wallet,
                                        _Region_Category=Region_Category,_joined_through_referral=joined_through_referral,_membership_category=membership_category,
                                        _preferred_offer_types=preferred_offer_types,_medium_of_operation=medium_of_operation,
                                        _internet_option=internet_option,_Discount=Discount,_Offer_Application_Preference=Offer_Application_Preference,_Past_Complaint=Past_Complaint,
                                        _Complatint_Status=Complatint_Status,_Feedback=Feedback,_prediction_method=prediction_method,_prediction = prediction) 
            results.save()
            return render(request,'/home/gunes/Bitirme/django-venv/src/churn/templates/results.html',{'results': prediction_result})

    return predict_result(prediction_method)