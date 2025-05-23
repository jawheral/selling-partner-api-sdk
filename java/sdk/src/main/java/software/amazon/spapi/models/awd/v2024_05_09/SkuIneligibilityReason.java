/*
 * The Selling Partner API for Amazon Warehousing and Distribution
 * The Selling Partner API for Amazon Warehousing and Distribution (AWD) provides programmatic access to information about AWD shipments and inventory.
 *
 * OpenAPI spec version: 2024-05-09
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.awd.v2024_05_09;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.Objects;

/** Represents the ineligibility reason for one SKU. */
@Schema(description = "Represents the ineligibility reason for one SKU.")
public class SkuIneligibilityReason {
    @SerializedName("code")
    private String code = null;

    @SerializedName("description")
    private String description = null;

    public SkuIneligibilityReason code(String code) {
        this.code = code;
        return this;
    }

    /**
     * Code for the SKU ineligibility.
     *
     * @return code
     */
    @Schema(required = true, description = "Code for the SKU ineligibility.")
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public SkuIneligibilityReason description(String description) {
        this.description = description;
        return this;
    }

    /**
     * Detailed description of the SKU ineligibility.
     *
     * @return description
     */
    @Schema(required = true, description = "Detailed description of the SKU ineligibility.")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        SkuIneligibilityReason skuIneligibilityReason = (SkuIneligibilityReason) o;
        return Objects.equals(this.code, skuIneligibilityReason.code)
                && Objects.equals(this.description, skuIneligibilityReason.description);
    }

    @Override
    public int hashCode() {
        return Objects.hash(code, description);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class SkuIneligibilityReason {\n");

        sb.append("    code: ").append(toIndentedString(code)).append("\n");
        sb.append("    description: ").append(toIndentedString(description)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
