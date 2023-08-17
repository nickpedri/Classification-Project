from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd
import acquire as ac


def train_val_test(df, strat, seed=100):
    train, val_test = train_test_split(df, train_size=0.7, random_state=seed, stratify=df[strat])
    val, test = train_test_split(val_test, train_size=0.5, random_state=seed, stratify=val_test[strat])
    return train, val, test


'''This function takes in a dataframe and splits the data into 3 separate dataframes containing 70%, 15% and 15% of 
the original data. It is used to split our data into a train, test, and validate sample.'''


def prep_iris(df):
    new_df = df.drop(columns=['species_id', 'measurement_id'])
    new_df = new_df.rename(columns={'species_name': 'species'})
    return new_df


'''This function prepares the iris dataset to be used by dropping two unnecessary columns and renaming the 
species column to something a little cleaner.'''


def prep_titanic(df):
    df = df.drop(columns=['passenger_id', 'pclass', 'embarked', 'deck'])
    df = pd.get_dummies(df, columns=['sex'], drop_first=True)
    df = pd.get_dummies(df, columns=['class', 'embark_town'])
    return df


'''This function prepares the titanic dataset to be used by dropping useless columns and creating dummies.'''


def titanic_dummies(df):
    df = pd.get_dummies(df, columns=['sex'], drop_first=True)
    df = pd.get_dummies(df, columns=['class', 'embark_town'])
    return df


'''This function creates dummies to some of the columns of the titanic dataset. It drops the first value of columns
with only two values and keeps all values for columns with more than two values.'''


def titanic():
    df = ac.titanic_data()
    impute_df(df, 'age', strategy='median')
    df = prep_titanic(df)
    return df


'''This function simply has all of the other functions combined to pull the data and transform it for usage all in
one function.'''


def prep_telco(df):
    telco = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id',
                             'streaming_tv', 'streaming_movies'])
    telco = pd.get_dummies(telco, columns=['gender', 'partner', 'dependents', 'phone_service',
                                           'paperless_billing', 'churn'], drop_first=True)
    rename = {'gender_Male': 'male', 'partner_Yes': 'partner', 'dependents_Yes': 'dependents',
              'phone_service_Yes': 'phone_service', 'paperless_billing_Yes': 'paperless_billing', 'churn_Yes': 'churn'}
    telco = telco.rename(columns=rename)
    telco = pd.get_dummies(telco, columns=['multiple_lines', 'online_security', 'online_backup', 'device_protection',
                                           'tech_support', 'contract_type', 'internet_service_type', 'payment_type'])
    to_delete = ['multiple_lines_No phone service', 'online_security_No internet service',
                 'online_backup_No internet service', 'device_protection_No internet service',
                 'tech_support_No internet service']
    telco = telco.drop(columns=to_delete)
    new_names = {'contract_type_Month-to-month': 'monthly_contract', 'contract_type_One year': 'year_contract',
                 'contract_type_Two year': 'two_year_contract', 'internet_service_type_DSL': 'DSL',
                 'internet_service_type_Fiber optic': 'Fiber_optic', 'internet_service_type_None': 'No_internet',
                 'payment_type_Bank transfer (automatic)': 'bank_transfer_pay',
                 'payment_type_Credit card (automatic)': 'credit_card_pay',
                 'payment_type_Electronic check': 'e-check_pay', 'payment_type_Mailed check': 'mailed_check'}
    telco = telco.rename(columns=new_names)
    telco = telco.drop(columns=['multiple_lines_No', 'online_security_No', 'online_backup_No', 'device_protection_No',
                                'tech_support_No'])
    names = {'multiple_lines_Yes': 'multiple_lines',
             'online_security_Yes': 'online_security',
             'online_backup_Yes': 'online_backup',
             'device_protection_Yes': 'device_protection',
             'tech_support_Yes': 'tech_support'}
    telco = telco.rename(columns=names)
    return telco


'''This function prepares the telco dataset. It will drop the id number columns since they are useless. Then it will
assign dummies to all of the columns with only two unique values since they would just be duplicates. The rest of the
categorical columns are also assigned dummies but every value is kept. Some of the columns are renamed so the table
is cleaner.'''


def split_x_y(df, target=''):
    x_df = df.drop(columns=target)
    y_df = df[target]
    return x_df, y_df


'''This function splits a dataframe by the target column. It takes two arguments: The dataframe containing all of the
 information, and the name of the column that must be split.'''


def impute_df(df, column='', strategy='mean'):
    imputer = SimpleImputer(strategy=strategy)
    imputer.fit(df[[column]])
    df[[column]] = imputer.transform(df[[column]])
    return df


'''This function is used to impute data. The takes three arguments: The dataframe that you want to impute, the name 
of the column you want to impute, and the strategy used to impute. The function will fit and impute and return the new
imputed dataframe.'''


def baseline(df, data='', target_value='', show_results=True):
    df['baseline'] = df[data].mode()[0]  # Creates a baseline prediction from the mode of the data
    b_acc = (df[data] == df['baseline']).mean()
    sub_rec = df[df[data] == target_value]  # Subset of all positive cases for recall
    b_rec = (sub_rec[data] == sub_rec['baseline']).mean()
    sub_bas_pre = df[df['baseline'] == target_value]
    if sub_bas_pre.empty:
        bas_pre = 0.0
    else:
        bas_pre = (sub_bas_pre[data] == sub_bas_pre['baseline']).mean()
    if show_results:
        print(f'Baseline accuracy is: {round(b_acc * 100, 2)}%.')
        print(f'Baseline recall is: {round(b_rec * 100, 2)}%.')
        print(f'Baseline precision is: {round(bas_pre * 100, 2)}%.')
        print()
    df.drop(columns=['baseline'], inplace=True)


'''This function will calculate the baseline model as well as the metric for that model. It takes in the dataframe
containing the data, the name of the data column, and the positive class or target value. It will calculate the mode
of the target value column and create a baseline model that always guesses the mode. Then it will calculate the 
accuracy, precision and recall of the baseline model.'''


def evaluate_model(dataframe, data='data column', model='Series', p_class='', show_results=True):
    df = dataframe
    df['model'] = model
    m_acc = (df[data] == df['model']).mean()
    sub_rec = df[df[data] == p_class]  # Subset of all positive cases for recall
    m_rec = (sub_rec[data] == sub_rec['model']).mean()
    s_pre = df[df['model'] == p_class]  # Subset of all positive guesses
    m_pre = (s_pre[data] == s_pre['model']).mean()
    if show_results:
        print(f'Model accuracy is: {round(m_acc * 100, 2)}%.')
        print(f'Model recall is: {round(m_rec * 100, 2)}%.')
        print(f'Model precision is: {round(m_pre * 100, 2)}%.')


''' This function will evaluate model performance. It will take in the dataframe containing all the information (such
as the train dataframe), the name of the column containing the data, a series of the model predictions, and the
positive class or target variable. The function will calculate the accuracy, precision and recall of the model.'''


def importance(training, model):
    imp = {'cols': training.columns,
           'importance': model.feature_importances_}
    return pd.DataFrame(imp).sort_values(by='importance', ascending=False)


'''This function calculates the importance of each feature for models. It takes in the dataframe with the data,
and the model object. It will return a dataframe with the importance of each feature.'''
