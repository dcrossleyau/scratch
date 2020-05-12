echo "Using bash ${BASH_VERSION}"

INPUT_PN="${GITHUB_WORKSPACE}/wf/repos.json"

echo "Processing JSON file ${INPUT_PN} ..."

readarray -t repo_list < <(jq -r '.repos[].name' < ${INPUT_PN})
count_total=$((${#repo_list[@]} -1))
echo "count_total=${count_total}"
echo ${repo_list[@]}

