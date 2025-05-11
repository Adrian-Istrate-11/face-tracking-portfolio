{{- define "face-tracking.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "face-tracking.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "face-tracking.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "face-tracking.labels" -}}
app.kubernetes.io/name: {{ include "face-tracking.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: Helm
{{- end -}}
