INPUT_PN="${GITHUB_WORKSPACE}/wf/repos.json"
OUTPUT_FN="output.txt"
jq -r '.repos[].name' < ${INPUT_PN} > ${OUTPUT_FN}
