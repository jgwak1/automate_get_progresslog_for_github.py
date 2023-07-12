# Automate the process of getting progress-logs so that can be directly uploaed to github
# 
# so that this can be reused for benign

import os
import shutil 

# -----------------------------------------------------------------------------------------------------
# e.g.
# sample_logs_parent_dirpath = "/home/jgwak1/tabby/Malware_logs_JY+Priti+Meng_Machine_7th_May_2023/malware_empire"
# save_progresslogs_dirpath = "/home/jgwak1/Malware_logs_JY+Priti+Meng_Machine_7th_May_2023__progress_logs_for_github/malware_empire__progress_logs_for_github"
# -----------------------------------------------------------------------------------------------------

# Write it to handle both formats.
#
# Example: 
#  (JY-format):
#      sample_logs_parent_dirpath
#         --> malware_empire
#              --> malware_empire_Exploit-Jenkins_unzipped_and_integrated
#                    --> malware_empire_Exploit_Jenkins
#                          --> progressid_command_mapping.txt

if __name__ == "__main__":

   sample_logs_parent_dirpath = "/home/jgwak1/tabby/Malware_logs_JY+Priti+Meng_Machine_7th_May_2023/malware_poshc2"
   save_progresslogs_dirpath = "/home/jgwak1/Malware_logs_JY+Priti+Meng_Machine_7th_May_2023__progress_logs_for_github/malware_poshc2__progress_logs_for_github"


   for sample_log_unzipped_and_integrated_dirname in \
      [ dirname for dirname in os.listdir( sample_logs_parent_dirpath ) if "unzipped_and_integrated" in dirname ]:

      # "<sample-name>_unzipped_and_integrated" directory has one subdirectory of <sample-name>
      sample_log_dirname = os.listdir( os.path.join(sample_logs_parent_dirpath, sample_log_unzipped_and_integrated_dirname) )[0]

      try:
         source = os.path.join( sample_logs_parent_dirpath, 
                                sample_log_unzipped_and_integrated_dirname,
                                sample_log_dirname,
                                "processid_command_mapping.txt" ) 
         destination = os.path.join( save_progresslogs_dirpath, f"{sample_log_dirname.lower()}" ) 

         shutil.copy(source, destination)
         
      except:
         raise RuntimeWarning(f"{sample_log_dirname} : something wrong with this. check")
      