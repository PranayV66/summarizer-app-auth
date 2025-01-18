{{/*
Return the name of the chart
*/}}
{{- define "summarize-ai-auth.name" -}}
{{ .Chart.Name }}
{{- end }}

{{/*
Return the full name for a resource, including the release name
*/}}
{{- define "summarize-ai-auth.fullname" -}}
{{ printf "%s-%s" .Release.Name (include "summarize-ai-auth.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}