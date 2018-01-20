# -*- coding: utf-8 -*-

jobListPath = 'canada_jobs_list.txt'
headerPath = 'header.txt'

header_file = open(headerPath, 'r')
header = header_file.read()
header_file.close()

jobList_file = open(jobListPath, 'r')
jobs = []
for job in jobList_file:
    jobs.append(job)    
jobs.sort(key=lambda x: x.lower())

readme_file = open('README.md', 'w')
readme_file.write(header)
for job in jobs:
    readme_file.writelines(job)
    
readme_file.close()