# Automate the process of getting progress-logs so that can be directly uploaed to github
# 
# so that this can be reused for benign

# This file is comaptible with Non-JY directory structures 
#  (Non-JY format):
#       sample_logs_parent_dirpath
#         --> Empire_logs
#              --> Out-ObfuscatedTokenCommand
#                 --> processid_command_mapping.txt

import os
import shutil 

# -----------------------------------------------------------------------------------------------------
# e.g.
# prefix_pattern = "malware_powershell_malware_bazaar"
# sample_logs_parent_dirpath = "/home/jgwak1/tabby/Apache_powershell_malware_logs/Malware_Bazaar_logs"
# save_progresslogs_dir = "/home/jgwak1/tabby/malware_bazar_progress_logs_for_github"
# -----------------------------------------------------------------------------------------------------


if __name__ == "__main__":

   sample_logs_parent_dirpath = "/home/jgwak1/tabby/Malware_logs_Priti_Machine_9th_May_2023__not_in_es/PoshC2_logs"
   prefix_pattern = "malware_poshc2"
   save_progresslogs_dirpath = "/home/jgwak1/Malware_logs_Priti_Machine_9th_May_2023__not_in_es__progress_logs_for_github/PoshC2_logs__progress_logs_for_github"


   for sample_log_dirname in os.listdir( sample_logs_parent_dirpath ):

      try:
         source = os.path.join( sample_logs_parent_dirpath, sample_log_dirname, "processid_command_mapping.txt" ) 
         destination = os.path.join( save_progresslogs_dirpath, f"{prefix_pattern}_{sample_log_dirname.lower()}" ) 

         shutil.copy(source, destination)
         
      except:
         raise RuntimeWarning(f"{sample_log_dirname} : something wrong with this. check")
      