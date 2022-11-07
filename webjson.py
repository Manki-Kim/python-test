from typing import Union

from fastapi import FastAPI, Response

app =  FastAPI()

@app.get("/")
async def read_root():
   ret_str = """{
   "deploy_type": "cluster",
   "status": "processing",
  "step_status" : "test\\nabc"
    }"""
   return Response(content=ret_str, media_type="application/json")


@app.get("/cm")
async def read_root():
   ret_str = """{
  "kind": "ConfigMap",
  "apiVersion": "v1",
  "metadata": {
    "name": "kubeconfig-user2",
    "namespace": "kubesphere-controls-system",
    "uid": "4bae90a0-9289-4e59-b48f-4aba82d85003",
    "resourceVersion": "2618222",
    "creationTimestamp": "2022-11-01T07:53:28Z",
    "labels": {
      "kubesphere.io/username": "user2"
    },
    "ownerReferences": [
      {
        "apiVersion": "iam.kubesphere.io/v1alpha2",
        "kind": "User",
        "name": "user2",
        "uid": "e9694104-8dd9-48c4-8edd-34ba689265da",
        "controller": true,
        "blockOwnerDeletion": true
      }
    ],
    "managedFields": [
      {
        "manager": "controller-manager",
        "operation": "Update",
        "apiVersion": "v1",
        "time": "2022-11-01T07:53:28Z",
        "fieldsType": "FieldsV1",
        "fieldsV1": {"f:data":{".":{},"f:config":{}},"f:metadata":{"f:labels":{".":{},"f:kubesphere.io/username":{}},"f:ownerReferences":{".":{},"k:{\\"uid\\":\\"e9694104-8dd9-48c4-8edd-34ba689265da\\"}":{".":{},"f:apiVersion":{},"f:blockOwnerDeletion":{},"f:controller":{},"f:kind":{},"f:name":{},"f:uid":{}}}}}
      }
    ]
  },
  "data": {
    "config": "apiVersion: v1\\nclusters:\\n- cluster:\\n    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM1ekNDQWMrZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeU1UQXhPVEExTXpNd04xb1hEVE15TVRBeE5qQTFNek13TjFvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTGhoCkhXNEY5M2Nib01zVUczZm1yaGZaZmkyNlk4SVpZeDNCK010VmliK1RmaEF3VERrMGdTdE1RZEsweklValo1c20KM3hhVER4aVdRV1B6bGIxOFJlY29QYSsvekxlSkM0dy9kL1Q1TnBBdEdhdDBrY1dwR084czdlVnRIYURzR3BlNAphSC83MWVDeExaWHFnTnd2T2VaRjFHSk9SMXNFSksrYnBPS3BONTNzT01uV0hQT0dPSWx1cURvd1J0YTUzTFN6CngreTJiek5TRkdpeTk5YmR1RENIc3RxUHJMYmpWN09xakpWTE5lSi9iV0wrWXpROGpvOWZyZng2UHJoQlFKNWcKYkJ6NHZUZ0JKS0k4UHdwanVsZDV5eE92NXVPb2dML0V6VlRMVTJmL1c5dFFJd1ZxM1B0aXR0MklVcER3UDJWaQpaaHk2c0VpdDBTZ2NueXpKLzhjQ0F3RUFBYU5DTUVBd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZLa21yblRISWZjZDc3WVFTSml5dW93d0dsdENNQTBHQ1NxR1NJYjMKRFFFQkN3VUFBNElCQVFBSU5LUWVwRTV6OHpWL3NkVkZ0amdQY2IwV2dlRVJPdFlER21JN2dQN2xIdjVFNGgrKwpwMzdXSzlZR09tM0FnV3JXelZkQ2d6eHNHWVczVG4yYXF5NTg4QVhyVVJwdG5zUHlTaysyazd3TGhla3BPeGQ1ClhHYWZyczl5WCswYUpRaGw0WkROaElXNUtDSnJZbHQvRll2RGFaTTF6YXk4K1FiZXI2RUFsS1puWHRhd2x3aU4Kc0l3VlNJa29qQjRKSFV6SmUvb2tUc1JmMzYzTk9zKzV5QmRJM3dQV1g1Rm9nVWN1NWN4RVVGcGNxQlRNUEYrNwo4VXpDeHd6V3VaVUZWU05jZ2ZhSlRwc0hWR1NHaDJub0gyMHA2ZGhXR0h1R2VPaGlIM0hicFloWjV1Qm93U2RYCjhvWE1aaDZVSXdTS3pEWFpRSm8zeEF3WHl2ZWp0WE55aEV2NgotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==\\n    server: https://10.96.0.1:443\\n  name: local\\ncontexts:\\n- context:\\n    cluster: local\\n    namespace: default\\n    user: user2\\n  name: user2@local\\ncurrent-context: user2@local\\nkind: Config\\npreferences: {}\\nusers:\\n- name: user2\\n  user:\\n    client-certificate-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCakNDQWU2Z0F3SUJBZ0lSQUxPb0tEdkhaOGFhOEx2dDlmNG1GTUV3RFFZSktvWklodmNOQVFFTEJRQXcKRlRFVE1CRUdBMVVFQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TWpFeE1ERXdOelE0TWpoYUZ3MHlNekV4TURFdwpOelE0TWpoYU1CQXhEakFNQmdOVkJBTVRCWFZ6WlhJeU1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBCk1JSUJDZ0tDQVFFQXozcG9GTklDOWdkNzIwNU5xbENpREFpQ1FTNlZJZjlUTGt6ZmR1WTJoL3FoMWhLUSsycmYKRlRyWHdncTNDYVg5U3pob1ZrLy8xcitNaXJtUCtSQmlBQlZFTDdFeXNSQnhsMjZvYmtKa2g0SUUwbkR5bjdXRApDd2RhNU8rT3dzWnVYUjlVMFIyVGM4OVVGTWtKZ2xuSE1wSXJ1ZHRoVTEzNVVpazRsejFzTHpQRXBsbW10SmpPCllXaWk2S2VnaXJiZ01aMUJ4bkg3b2pRM2lZbVFXTHVJQ3B4RUQ4T0h6cFJQODJlaERPckxIZ3kzRkZhUTBjVWgKa2JZUWdKUXZ4RTU4WS83L0RCUDdWVFcxZHlPRU9nWks5YWFsMnpNRzJQRDczK0kzdWdSbWVNak8zRHNhdVljeQo5RGxhaGxYbDBDRmhJLzdrdnQ2dlJUV21EaVZ2TDc5OEp3SURBUUFCbzFZd1ZEQU9CZ05WSFE4QkFmOEVCQU1DCkJhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUhBd0l3REFZRFZSMFRBUUgvQkFJd0FEQWZCZ05WSFNNRUdEQVcKZ0JTcEpxNTB4eUgzSGUrMkVFaVlzcnFNTUJwYlFqQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUFudGtNNFJEcwo4WlF3dmNrazhJRGlSU1J2ZnV0QjZLQ2MvTTU0UytGc2FBVytLT0ZhNERDMU9nWGZjWlhPK0s3TFdPOHp5L2QrClBORlQ0enVEY1FwczAxTVEzWGpLU0g1bktudGI2RzhuUkNXQTNPWG05MVJlMjUxUlVGVVJjNlE2VDhyam1pQTEKTzQveEtPU0N2UVlJMEE2ZU4xMy9HQW9xWm5QSkNIamM5ek9kVlFmanNnZFFLVUxRMXliT0NrREk1YU55UlhHdQplOHlxSnB2SGxyQW9UaVN0OThlUDJuc0k3ZE94RmlwQUpxQjB1R3RHUFIyYzNDUEZ4MENuUUFvSGFLYmQ1ellCCjFRM1RkenZRaGltWE1TMnVFRWd4UnFGTmRBVkF6eWgycnF1ajQ3eW9qSFdBY0VjbTI1SVFySi9jZjFxbEtWWncKazF2Vm5haVBhcFQ3Ymc9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==\\n    client-key-data: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUVwQUlCQUFLQ0FRRUF6M3BvRk5JQzlnZDcyMDVOcWxDaURBaUNRUzZWSWY5VExremZkdVkyaC9xaDFoS1EKKzJyZkZUclh3Z3EzQ2FYOVN6aG9Way8vMXIrTWlybVArUkJpQUJWRUw3RXlzUkJ4bDI2b2JrSmtoNElFMG5EeQpuN1dEQ3dkYTVPK093c1p1WFI5VTBSMlRjODlVRk1rSmdsbkhNcElydWR0aFUxMzVVaWs0bHoxc0x6UEVwbG1tCnRKak9ZV2lpNktlZ2lyYmdNWjFCeG5IN29qUTNpWW1RV0x1SUNweEVEOE9IenBSUDgyZWhET3JMSGd5M0ZGYVEKMGNVaGtiWVFnSlF2eEU1OFkvNy9EQlA3VlRXMWR5T0VPZ1pLOWFhbDJ6TUcyUEQ3MytJM3VnUm1lTWpPM0RzYQp1WWN5OURsYWhsWGwwQ0ZoSS83a3Z0NnZSVFdtRGlWdkw3OThKd0lEQVFBQkFvSUJBUUNTbmxUNUNhUXdDdi9hCjdjM3lvc0t4TUQ0a0kvQWRzMW9yNlFVdDkrZm5WaFdSdTFNYmFOMjNHZnNvMC91ZlpON0hqbGdsVHFsa0w3NzQKdGNOcFpjdHJkWnZXL0NqdmVjaGNGRVlRalBpUHpqRHNLZ2M3RjhGQVJQVlZ2WGlzYWgvSnpQOWFPOFZjM05IMQpVbEJXL216SGJ3WlpkQSttSTAyeVl4RHJ4K3N3dXVUSUVJMWN2bVVVU2JTRkdMWnpZSm9uTmQ5b1IxWWZkeHJTCklZSzlBdVhORHVjZTlBUGhHdmdoOWU4RUdYY3ptUzRxNHV2TTVGdktOUUFNWXZxSUZMeGFEcklKdmtIcHF3eTEKTG9VZkYweGFjQzE4c1pkTm1WQ1lMOWFRckozb2JlRUt5NDhqTVpzUXVLREJKYUJxYlBkTHFRRUhXZW1CZUl6agp2eUtsQjB6UkFvR0JBTlB4ZksrL1FnUitrQXREeTBYdkM0ajJkWHJodWF1K2dMM05HSHB1NmozNEZSbWJLSlpBCmtld0lIdFkwWEs3WTdyZDZ6MUlQeXVoYUg4dkovbWMrMkdnT204ek9sOXVyandKY1pmQXdnRVhyUzJzYWVadG8KdG5LVzIxcU9kUnYzUzVNWG9McTI5RGJ6NnZsZElsaTl5clVsd3VtNTI1QjYyM21IbE5IaU5BWFpBb0dCQVBxYgpUcU0xUFU2dGMxbU1Semk5YlJTVWlzb2RmV25JSjkvUUpyN2NtbUVQMnJGSHRaT1Zzdlo3NHRvMlpRV21rb0ZNCmtTUXJ4UGQvRGZlZzdZTXFoOWtwWXpJYTV3dktseU1vcHZyUWFsNC9GTTE5UnFrOGFOTElkcDlZdVl2ZWw0SlUKWlJRSGFZZ0wrMjlvSmN1V3JFQjBva3J2akgrbmNmSTRCSG40TkZIL0FvR0FVK3ZFOFZvTDYvZXBWYXlNYXE2UwpwTExpSmJ3SFp1ZlIxbFhGb1lVVm4yQUNDdGVUSkp1QXJETXk4cUpkS0thaEwybWplZHppL1VuaVdURXNXUGxiCmV5aDlySVVKUUdRWUJsbEx5K1dJaFNiNy8vYkZ2REdrUEk5Ylgrb1VtUFE4cW91cWl3UXlneWZtSE1NeC9HMTYKUEd3dFY1ck9ROUZCNGtjN09EZ1hYVkVDZ1lCa2ExbE9jdVgzSWUvSDRUc2sxRnJpVlVkc0IvY2FMVGMxS3Y1cgptcEJOOW9GbWFscXJJZUJOZm9UL2RhNXpYalQwbE03UUZLM2Zrc3p3L2s1T01mdXZuRE1BZitFM1MxM1dtOUtWClRIQmpCWm43WVlpd0JlSG5IS2JUNFVTd2RHaDN0QU93eSt1UXRXUnlWdVJXT1RFYXZ1SE5iMEg0WVF0NnlOR2EKWWtmczF3S0JnUUNjc2xkbjRpbWw4b2VMbEZwanp0aStwZEE1cG52UUFlWmRIbTRXYkltVEhiTytFYnphZlJJMQpVYnp0Q0FOVDRFelBZSkZXL1c1UmJLMzdKWVYzK0hGcEJTdFphRTRqTkV1Sjk2bzM0YTJDdnNPcTZqNmd3dU9tCjFndm5LdjdGYkJjR1lOTFZEdE4zQjdQNHhhVDUxRy9rM244cEIvMVJZQWNxL3Q0Q0N3VjVpdz09Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0K\\n"
  }
}"""
   return Response(content=ret_str, media_type="application/json")