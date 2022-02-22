aws-sandbox helm upgrade --namespace=ops \
 zebra-statserve-ops zebra-statserve \
  --install --history-max 10 \
   --set 'annotations.app\.gitlab\.com/app=thezebra-libraries-zebra-statserve' --set 'annotations.app\.gitlab\.com/env=ops' \
    --set 'image.pullSecrets[0]=docker-registry-config' \
    --set 'image.pullSecrets[1]=gitlab-registry-config' \
     --set image.repository=registry.gitlab.com/thezebra/libraries/zebra-statserve \
      --set image.tag=main \
 --values ../vars/dev/values.yaml
