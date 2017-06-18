# -*- coding: utf_8 -*-

import setting
from StaticAnalyzer import static_analyzer

root_dir = setting.get_root_dir()
analysis_dir = setting.get_analysis_home()
save_dir = setting.get_save_home()
error_dir = setting.get_error_home()
upload_dir = setting.get_upload_home()
download_dir = setting.get_download_home()
reAnalysis_dir = setting.get_reAnalysis_home()

static_analyzer.checkFile(download_dir)
static_analyzer.analysis(analysis_dir)
