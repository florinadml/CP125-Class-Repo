def audit_zero_trust(baseline_set, current_log_list):
   log_set = set(current_log_list)

   authorized = baseline_set & log_set 

   alerts = log_set - baseline_set 

   inactive =  baseline_set - log_set 

   return (authorized, alerts, inactive)