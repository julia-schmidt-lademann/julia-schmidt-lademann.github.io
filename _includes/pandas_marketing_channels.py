# Create a python script that attributes the registration to a given marketing channel, based on the “Last Sent” attribution model. The time windows that we have for each marketing channel are the following ones:
# 30 days for Direct Mail.
# 3 days for SMS, both acquisition and CRM.
# 3 days for Email, both acquisition and CRM.
# For this exercise you can assume that Tables A, B, and C are Pandas dataframes.


# filtering
import pandas as pd

marketing = pd.DataFrame() #let's assume we want to track the effectiveness of different campain_name's
events= pd.DataFrame()
events=events[(events["event"]=="activation")]
marketing = marketing.groupby('touchpoint_date').last()

result = pd.merge(events, marketing, on="customer_id")
result['date_diff']=result['event_date']-result['touchpoint_date']
direct_mail = result[(result["marketing_channel"]=="direct_mail")&(result["date_diff"]<=30)]
sms = result[((result["marketing_channel"]=="acquisition_sms")|(result["marketing_channel"]=="crm_sms"))&(result["date_diff"]<=3)]
email = result[((result["marketing_channel"]=="acquisition_email")|(result["marketing_channel"]=="crm_email"))&(result["date_diff"]<=3)]

direct_mail_summary = direct_mail.groupby('campain_name').count()
sms_summary = direct_mail.groupby('campain_name').count()
email_summary = direct_mail.groupby('campain_name').count()
signups = direct_mail_summary.append(sms_summary, ignore_index=True)
signups = signups.append(email_summary, ignore_index=True)
touchpoints = marketing.groupby('campain_name').count()

# Summary table containing the signups out of all touchpoints per campaign to compare their effectiveness.
result = pd.merge(touchpoints, signups, on="campain_name")
