from simple_salesforce import Salesforce
import constants as const
import base64 as bs


def get_data(case_number):
    try:
        sales_force_login = Salesforce(username=const.username, password=bs.b64decode(const.password).decode("utf-8"),
                                       security_token=bs.b64decode(const.security_token).decode("utf-8"))

        case_details = sales_force_login.bulk.Case.query(const.query + str(case_number) + "'")

        if not case_details:
            out_data = {'message': 'Case number is not present'}
            return out_data
        else:
            case_id = case_details[0].get('Id')
            account_type = case_details[0].get('Account_Type__c')
            priority = case_details[0].get('Priority')
            case_link = const.case_permalink.format(case_id)
            case_number = case_details[0].get('CaseNumber')
            subject = case_details[0].get('Subject')
            out_data = {'caseNumber': case_number, 'accountType': account_type, 'priority': priority, 'subject': subject,
                        'case_link': case_link}
            return out_data

    except Exception as err:
        out_data = {'exception': 'Exception has occured',
                    'text': err}
        return out_data





