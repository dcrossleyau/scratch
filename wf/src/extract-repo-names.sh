INPUT_PN="${GITHUB_WORKSPACE}/wf/repos.json"
jq -r '.repos[].name' < ${INPUT_PN}
