import datetime

from src.data.default import authotizations
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser


def add_create_at_timestamp(data: object, is_log: bool = False) -> object:
    if is_log:
        data.log = datetime.datetime.now().astimezone().isoformat()
    else:
        data.create_at = datetime.datetime.now().astimezone().isoformat()
    return data


def check_authorization(db, user, authorization_list):
    classifier_id = user.User.classified_as
    classifier_obj = RepositoryClassifierUser(db).searchById(classifier_id)
    authorization_id = classifier_obj.ClassifierUser.authorization_id
    for k, v in authotizations.items():
        if authorization_id == int(k):
            if v in authorization_list:
                return True
    return False


email_body_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-mail - Conecta Age</title>
</head>
<body style="margin: 0; padding:0; font-family: Arial, Helvetica, sans-serif;" >
    <table border="0" width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <!---------Header------>
                <table align="center" border="0" width="600px" cellpadding="0" cellspacing="0">
                    <tr>
                        <td bgcolor="#002f71" align="center" style="padding: 60px 0 50px 0;">
                            <img src="https://i.imgur.com/XTPbFEl.png" alt="" width="436" height="194">
                        </td>
                    </tr>
                    <!-----Corpo---->
                    <tr>
                        <td bgcolor="#fff" align="center">
                            <table border="0" width="600px" cellpadding="0" cellspacing="0" style="padding: 15px; color: #002f71;" >
                                <tr align="center">
                                    <td>
                                        <h1>Seu Codigo de Autenticação</h1>
										<h1>YOUR_CODE_HERE</h1>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <!-----Footer----->
                    <tr>
                        <td bgcolor="#CC6A0B" style="padding: 20px;">
                            <table border="0" width="600px" cellpadding="0" cellspacing="0">
                                <tr align="center">
                                    <td width="85%">
                                        <span style="color: #fff;">www.age.pe.gov.br</span>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
